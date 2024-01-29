import os
from dektools.file import write_file, remove_path
from ..artifacts.helm import HelmCommonArtifact, HelmCodingArtifact, HelmGitArtifact, get_artifact_helm_by_url
from .base import AllInOneBase


class AllInOneHelm(AllInOneBase):
    def build(self, item, image):
        self.artifact_src.pull(item)
        _, chart, version = self.artifact_src.url_parse(item)
        path_tgz = self.artifact_src.package(chart, version)
        path_docker = os.path.join(os.path.dirname(path_tgz), 'Dockerfile')
        name_tgz = os.path.basename(path_tgz)
        write_file(path_docker, f"FROM scratch\nADD {name_tgz} /charts/{name_tgz}")
        self.artifact_all_in_one.build(image, path_docker)
        remove_path(path_docker)
        remove_path(path_tgz)


class HelmCommonAllInOne(AllInOneHelm):
    artifact_src_cls = HelmCommonArtifact


class HelmCodingAllInOne(AllInOneHelm):
    artifact_src_cls = HelmCodingArtifact


class HelmGitAllInOne(AllInOneHelm):
    artifact_src_cls = HelmGitArtifact


def get_helm_all_in_one_by_url(url):
    artifact_helm = get_artifact_helm_by_url(url)
    for cls in [HelmCommonAllInOne, HelmCodingAllInOne, HelmGitAllInOne]:
        if cls.artifact_src_cls is artifact_helm:
            return cls
