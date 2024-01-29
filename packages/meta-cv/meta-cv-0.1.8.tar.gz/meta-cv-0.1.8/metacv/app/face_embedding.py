import time
from ..utils import preprocess


class FaceEmbedding:
    def __init__(self,
                 model_path: str,
                 input_width: int,
                 input_height: int,
                 use_preprocess=True,
                 pad=None,
                 normal=None,
                 mean=None,
                 std=None,
                 swap=None,
                 confidence_thresh=None,
                 nms_thresh=None,
                 class_names=None):
        self.model_path = model_path
        self.input_width = input_width
        self.input_height = input_height
        self.use_preprocess = use_preprocess
        self.pad = pad
        self.normal = normal
        self.mean = mean
        self.std = std
        self.swap = swap
        self.confidence_thresh = confidence_thresh
        self.nms_thresh = nms_thresh
        self.class_names = class_names
        self.model = None
        self.det_output = None

    def initialize_model(self):
        # todo 该函数由子类实现
        pass

    def infer(self, image):
        # todo 该函数由子类实现
        # self.outputs:
        # det_output: [batch_size, class_num]
        pass

    def predict(self, image):
        s = time.time()
        if isinstance(image, list):
            if self.use_preprocess:
                img = [preprocess(im, (self.input_height, self.input_width), self.pad, self.normal, self.mean,
                                  self.std, self.swap)[0] for im in image]
            else:
                img = image
        else:
            if self.use_preprocess:
                img = preprocess(image, (self.input_height, self.input_width), self.pad, self.normal, self.mean,
                                 self.std, self.swap)[0]
            else:
                img = image
        print("preprocess: ", time.time() - s)

        s = time.time()
        self.infer(img)
        print("infer: ", time.time() - s)

        s = time.time()
        embedding = self.det_output  # self.det_output.flatten()
        print("postprocess: ", time.time() - s)

        return embedding
