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
        pass

    if content != current:
        with open(filename, 'w') as write_handle:
            write_handle.write(content)
        print('++', filename)
