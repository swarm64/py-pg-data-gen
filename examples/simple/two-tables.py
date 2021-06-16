
from lib.base_object import Dependency


TABLES = {
    'public.a': 'examples/simple/a.sql',
    'public.b': 'examples/simple/b.sql'
}

GRAPH = {
    'public.a': [
        Dependency(name='public.b', scaler=0.1)
    ],
    'public.b': []
}

ENTRYPOINT = Dependency('public.a', 1)
