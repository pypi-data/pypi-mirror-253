import cv2
import time
import numpy as np
from ..utils import preprocess, softmax, normalizion


class Classification:
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
        dets, det_scores, det_labels = [], [], []
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

        assert self.det_output.shape[-1] == len(self.class_names), "infer det output shape is not match"

        s = time.time()
        output_score = np.array([softmax(p) for p in self.det_output])
        output_class = np.argmax(output_score, axis=1)

        for label, score in zip(output_class, output_score):
            dets.append(self.class_names[int(label)])
            det_scores.append(float(score[int(label)]))
            det_labels.append(int(label))
        print("postprocess: ", time.time() - s)

        return dets, det_scores, det_labels

    def feature(self, image):
        s = time.time()
        if isinstance(image, list):
            if self.use_preprocess:
                outputs = [preprocess(im, (self.input_height, self.input_width), self.pad, self.normal, self.mean,
                                      self.std, self.swap)[0] for im in image]
                img, ratio = [out[0] for out in outputs], outputs[0][1]
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
        features = normalizion(self.det_output, axis=1)
        print("postprocess: ", time.time() - s)

        return features

    def show(self, image, dets, det_scores, det_labels):
        if dets is None or len(dets) == 0:
            return image
        for det, score, label in zip(dets, det_scores, det_labels):
            print(self.class_names[label], score)
            cv2.putText(image, '%s(%.2f)' % (self.class_names[label], score),
                        (0, 20),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1,
                        (0, 255, 0),
                        thickness=1)
