import os
import functools
import shutil


class ArtifactBase:
    typed = ''
    marker_registry = 'registry'
    default_registry_key = ''

    cli_list = []

    def __init__(self, environ=None):
        self.environ = environ or os.environ

    def prepare(self):
        pass

    @property
    @functools.lru_cache(None)
    def path_work(self):
        return os.path.join(os.path.expanduser('~'), f'.dekartifacts', self.typed)

    @property
    @functools.lru_cache(None)
    def cli(self):
        for cli in self.cli_list:
            if shutil.which(cli):
                return cli

    def query_env_map(self, marker, is_end):
        result = {}
        for key in self.environ.keys():
            if is_end:
                if key.endswith(marker):
                    result[key[:-len(marker)]] = self.environ[key]
            else:
                if key.startswith(marker):
                    result[key[len(marker):]] = self.environ[key]
        return result

    def list_env_registries(self):
        return sorted(self.query_env_map(f"__{self.typed}_{self.marker_registry}", True))

    def login_all_env(self):
        for registry in self.list_env_registries():
            self.login_env(registry)

    def login_env(self, registry):
        registry = registry or self.environ.get(self.default_registry_key, '')
        kwargs = self.query_env_map(f"{registry}__{self.typed}_", False)
        self.login(**kwargs)

    def login(self, **kwargs):
        raise NotImplementedError
