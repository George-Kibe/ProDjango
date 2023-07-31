import yaml
from django.conf import settings
from django.db import transaction


def apply_on_commit(callable_):
    if settings.USE_ON_COMMIT_HOOK:
        transaction.on_commit(callable_)
    else:
        callable_()


def yaml_coerce(value):
    # convert value to propert python
    if isinstance(value, str):
        # yaml.load returns a Python Object
        # converts string dict "{'apples': 1, 'bacon':4}"  to a dict
        # useful beacuse we need to stringify settings in dockerfiles
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value