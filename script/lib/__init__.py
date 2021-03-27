import os


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
