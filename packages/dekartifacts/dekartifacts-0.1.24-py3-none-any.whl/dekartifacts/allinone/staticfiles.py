import os
from dektools.file import write_file, remove_path
from ..artifacts.staticfiles import StaticfilesArtifact
from .base import AllInOneBase


class StaticfilesAllInOne(AllInOneBase):
    artifact_src_cls = StaticfilesArtifact

    def build(self, item, image):
        path_file_raw = self.artifact_src.pull(item)
        path_file = write_file(None, t=True, m=path_file_raw)
        path_dir = os.path.dirname(path_file)
        path_docker = os.path.join(path_dir, 'Dockerfile')
        write_file(
            path_docker,
            s=f"FROM scratch\nADD {os.path.basename(path_file)} "
              f"{self.artifact_src.path_keep_dir('/staticfiles', path_file_raw)}"
        )
        self.artifact_all_in_one.build(image, path_docker)
        remove_path(path_docker)
        remove_path(path_file)
