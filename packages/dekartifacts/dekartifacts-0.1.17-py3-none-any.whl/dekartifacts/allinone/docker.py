from ..artifacts.docker import DockerArtifact
from .base import AllInOneBase


class DockerAllInOne(AllInOneBase):
    artifact_src_cls = DockerArtifact

    def build(self, item, image):
        self.artifact_src.pull(item)
        self.artifact_src.tag(item, image)

    def remove(self, item):
        self.artifact_src.remove(item)

    def entry(self, url):
        return self.artifact_src.entry(
            f'{self.rr_all_in_one}:{self.artifact_src.url_to_tag(self.artifact_src.full_url(url))}'
        )
