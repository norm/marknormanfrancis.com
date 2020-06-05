import os
import toml


def update_toml(filename, data):
    subdir = os.path.dirname(filename)
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    current = ''
    try:
        with open(filename, 'r') as handle:
            current = handle.read()
    except FileNotFoundError:
        pass

    if toml.dumps(data) != current:
        with open(filename, 'w') as toml_handle:
            toml.dump(data, toml_handle)
        print('++', filename)
