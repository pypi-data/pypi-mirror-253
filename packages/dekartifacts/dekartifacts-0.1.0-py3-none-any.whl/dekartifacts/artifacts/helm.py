import json
import os
import string
import functools
from dektools.shell import shell_with_input, shell_wrapper
from dektools.file import sure_dir, remove_path, write_file, read_text
from .base import ArtifactBase


class ArtifactHelm(ArtifactBase):
    typed = 'helm'
    cli_list = ['helm']

    @staticmethod
    def registry_to_repo(registry):
        valid = string.digits + string.ascii_letters
        result = ""
        for x in registry.split(":")[-1]:
            if x not in valid:
                x = '-'
            result += x
        return result.strip('- ')

    @staticmethod
    def url_parse(url):
        registry, chart_and_version = url.split('::')
        chart, version = chart_and_version.split(':')
        return registry, chart, version

    @property
    @functools.lru_cache(None)
    def path_charts(self):
        return os.path.join(self.path_work, 'charts')

    def pull(self, url):
        registry, chart, version = self.url_parse(url)
        path_chart = os.path.join(self.path_charts, chart)
        sure_dir(path_chart)
        remove_path(path_chart)
        shell_wrapper(
            f'{self.cli} fetch {self.registry_to_repo(registry)}/{chart} '
            f'--version {version} --untar --untardir {self.path_charts}'
        )
        shell_wrapper(f'{self.cli} dependency update {path_chart}')

    def package(self, url):
        registry, chart, version = self.url_parse(url)
        path_chart = os.path.join(self.path_charts, chart)
        path_tgz = os.path.join(os.getcwd(), f"{chart}-{version}.tgz")
        shell_wrapper(f"{self.cli} package {path_chart}")
        return write_file(None, t=True, m=path_tgz), registry

    def entry(self, url):
        registry, chart, version = self.url_parse(url)
        return dict(
            netloc=registry,
            name=chart,
            ref=chart,
            version=version
        )


class HelmCodingArtifact(ArtifactHelm):
    typed = 'helm_coding'

    def prepare(self):
        shell_wrapper(f"{self.cli} plugin install https://e.coding.net/coding-public/helm-push/helm-coding-push")

    def login(self, registry='', username='', password=''):
        print(F"Login to {registry} {username[0]}***{username[-1]}")
        ret, _, err = shell_with_input(
            f"{self.cli} repo add "
            f"--username {username} "
            f"--password-stdin {self.registry_to_repo(registry)} '{registry}'",
            password)
        if ret:
            raise ChildProcessError(err)

    def push(self, url):
        path_tgz, registry = self.package(url)
        shell_wrapper(f"{self.cli} coding-push {path_tgz} {self.registry_to_repo(registry)}")
        remove_path(path_tgz)


class HelmGithubPagesArtifact(ArtifactHelm):
    typed = 'helm_git'

    @property
    @functools.lru_cache(None)
    def path_auth(self):
        return os.path.join(self.path_work, 'auth.json')

    def login(self, host='', email='', username='', password=''):
        auth = {}
        if os.path.exists(self.path_auth):
            auth = json.loads(read_text(self.path_auth))
        auth[host] = [email, username, password]
        write_file(self.path_auth, s=json.dumps(auth))

    def auth_from_local(self, host):
        if os.path.exists(self.path_auth):
            auth = json.loads(read_text(self.path_auth))
            email, username, password = auth[host]
            shell_wrapper(f'git config --global user.name "{username}"')
            shell_wrapper(f'git config --global user.email "{email}"')
            shell_wrapper(f'git config --global user.password "{password}"')
