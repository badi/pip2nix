
import os.path
import pkg_resources

import yaml
from munch import munchify


def read(path=None, inputs=None, setupRequires=None, buildInputs=None):

    defaults = pkg_resources.resource_string(__name__, 'data/nix-pip.rc')
    default = yaml.load(defaults)

    if path and os.path.exists(path):

        with open(path) as fd:
            cfg = yaml.load(fd)

    else:
        cfg = default

    if inputs:
        cfg['requirements']['inputs'] = inputs

    if setupRequires:
        cfg['setup_requires'].update(setupRequires)

    if buildInputs:
        cfg['build_inputs'].update(buildInputs)

    return munchify(cfg)


if __name__ == '__main__':
    import sys

    try:
        print read(sys.argv[1])
    except IndexError:
        print read()
