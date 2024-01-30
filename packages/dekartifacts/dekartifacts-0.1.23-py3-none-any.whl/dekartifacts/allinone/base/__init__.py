from ...artifacts.docker import DockerArtifact


class AllInOneBase:
    artifact_all_in_one_cls = DockerArtifact
    artifact_src_cls = None

    def __init__(self, rr_all_in_one, environ=None):
        self.rr_all_in_one = rr_all_in_one
        self.artifact_all_in_one = self.artifact_all_in_one_cls(environ)
        self.artifact_src = self.artifact_src_cls()

    def prepare(self):
        self.artifact_all_in_one.prepare()
        self.artifact_src.prepare()

    def push(self, items):
        exist_tags = self.artifact_all_in_one.remote_tags(self.rr_all_in_one)
        for i, item in enumerate(items):
            print(f"\npushing progress: {i + 1}/{len(items)} \nitem: {item}", flush=True)
            image = f"{self.rr_all_in_one}:{self.artifact_all_in_one.url_to_tag(item)}"
            if image.split(':')[-1] in exist_tags:
                print(f"skip pushing as exist: {item}", flush=True)
                continue
            self.build(item, image)
            self.artifact_all_in_one.push(image)
            self.artifact_all_in_one.remove(image)
            self.remove(item)

    def build(self, item, image):
        raise NotImplementedError

    def remove(self, item):
        pass
