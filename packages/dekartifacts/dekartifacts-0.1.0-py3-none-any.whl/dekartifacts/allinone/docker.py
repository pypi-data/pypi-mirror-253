from ..artifacts.docker import DockerArtifact
from .base import AllInOneBase


class DockerAllInOne(AllInOneBase):
    artifact_src_cls = DockerArtifact

    def build(self, item, image):
        self.artifact_src.pull(item)
        self.artifact_src.tag(item, image)

    def remove(self, item):
        self.artifact_src.remove(item)
