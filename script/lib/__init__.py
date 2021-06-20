import os
import re
import toml

from django.utils.text import slugify


def update_content(filename, content):
    subdir = os.path.dirname(filename)
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    current = ''
    try:
        with open(filename, 'r') as handle:
            current = handle.read()
    except FileNotFoundError:
        current = None

    if content != current:
        with open(filename, 'w') as write_handle:
            write_handle.write(content)
        if not current:
            print('++', filename)
        else:
            print('--', filename)

def strip_trailing_hashtags(text):
    """
    Remove hashtags from the end of a string, but not from the middle.
    """
    if not text:
        return ''
    words = [
        word 
        for word in text.split(' ')
        if word
    ]
    if words[-1].startswith('#'):
        while words and words[-1].startswith('#'):
            del words[-1]
    return ' '.join(words)


def strip_links(text):
    if not text:
        return ''
    words = [
        word
        for word in text.split(' ')
        if word
    ]
    while words and (words[-1].startswith('http://') or words[-1].startswith('https://')):
        del words[-1]
    return ' '.join(words)


def get_markdown_data(file):
    with open(file) as handle:
        content = handle.read()
    marker = content[0:3]
    end_marker = content[4:].find(marker) + 4
    markdown_start = end_marker + 5
    return (toml.loads(content[4:end_marker]), content[markdown_start:])


def get_frontmatter_from_markdown(file):
    front, body = get_markdown_data(file)
    return front


def get_body_from_markdown(file):
    front, body = get_markdown_data(file)
    return body


def tagify(text):
    # turn CamelCase into hyphenated
    text = re.sub(r'([a-z\W])([A-Z0-9])', r'\1-\2', text)
    text = slugify(text)
    return text.replace('_', '-')
