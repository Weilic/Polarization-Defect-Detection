
from defectdetector.transforms import BaseTransform, Transforms
from defectdetector.detector import Detector


class Pipeline:

    def __init__(self,
                 pipeline=None,
                 ):
        self.pipeline = self.setup(pipeline)

    def setup(self, pipeline):
        _pipeline = []

        for i, p in enumerate(Transforms.METHOD):
            if p in pipeline:
                _pipeline.append(Transforms.METHOD[i])
        return _pipeline

    def add(self, processor):
        print(type(processor))
        self.pipeline.append(processor)

    def remove(self, name):
        for i, p in enumerate(self.pipeline):
            if p.__class__.__name__ == name:
                del self.pipeline[i]
                return True
        return False

    def run(self, frame):
        for p in self.pipeline:
           frame = p()(frame)
        return frame