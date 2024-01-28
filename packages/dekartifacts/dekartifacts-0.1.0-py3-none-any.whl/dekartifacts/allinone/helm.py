import os
from dektools.file import write_file, remove_path
from ..artifacts.helm import ArtifactHelm
from .base import AllInOneBase


class HelmAllInOne(AllInOneBase):
    artifact_src_cls = ArtifactHelm

    def build(self, item, image):
        self.artifact_src.pull(item)
        path_tgz, _ = self.artifact_src.package(item)
        path_docker = os.path.join(os.path.dirname(path_tgz), 'Dockerfile')
        name_tgz = os.path.basename(path_tgz)
        write_file(path_docker, f"FROM scratch\nADD {name_tgz} /chart/{name_tgz}")
        self.artifact_all_in_one.build(image, path_docker)
        remove_path(path_docker)
        remove_path(path_tgz)
