from hashlib import md5
import mimetypes

import boto3
import requests

mimetypes.init()


class Bucket(object):
    def __init__(self, bucket_name):
        self.bucket = boto3.resource('s3').Bucket(bucket_name)
        self.bucket_objects = dict()
        self.get_bucket_content()

    def get_bucket_content(self):
        for object in self.bucket.objects.all():
            self.bucket_objects.update({object.key: object})

    def upload_file(self, source, destination, check_digest=True, mimetype=None):
        if not check_digest and destination in self.bucket_objects:
            return False

        if source.startswith('http:') or source.startswith('https:'):
            req = requests.get(source)
            content = req.content
        else:
            content = open(source, 'rb').read()

        digest = '"%s"' % md5(content).hexdigest()
        if not mimetype:
            mimetype, _ = mimetypes.guess_type(source)

        if destination.startswith('/'):
            destination = destination[1:]

        # upload the file unless it matches what is already on S3
        upload = True
        try:
            if digest == self.bucket_objects[destination].e_tag:
                upload = False
        except KeyError:
            pass

        if upload:
            upload_args = {
                'Key': destination,
                'ACL': 'public-read',
                'Body': content,
                'ContentType': mimetype,
            }
            self.bucket.put_object(**upload_args)

        return upload
