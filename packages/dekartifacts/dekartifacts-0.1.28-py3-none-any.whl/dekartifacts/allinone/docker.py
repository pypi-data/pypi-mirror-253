from dektools.file import sure_dir
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
        return self.artifact_src.entry(self.url_mage(url))

    def fetch(self, items, path):
        sure_dir(path)
        tags = self.artifact_all_in_one.remote_tags(self.rr_all_in_one)
        for item in items:
            tag = self.artifact_src.url_to_docker_tag(item)
            if tag in tags:
                image = self.artifact_all_in_one.pull(self.url_mage(item))
                self.artifact_all_in_one.tag(image, item)
                self.artifact_all_in_one.remove(image)
            else:
                self.artifact_src.pull(item)
            self.artifact_src.exports(item, path)
        for item in items:
            self.artifact_src.remove(item)
