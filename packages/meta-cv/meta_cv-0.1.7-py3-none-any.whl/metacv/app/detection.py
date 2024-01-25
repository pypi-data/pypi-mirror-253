import cv2
import time
from ..utils import preprocess, postprocess


class Detection:
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
        # det_output: [1, 4 + 80, 6300]
        pass

    def predict(self, image):
        total_dets, total_scores, total_labels = [], [], []
        s = time.time()
        if isinstance(image, list):
            batch_size = len(image)
            if self.use_preprocess:
                outputs = [preprocess(im, (self.input_height, self.input_width), self.pad, self.normal, self.mean,
                                      self.std, self.swap) for im in image]
                img, ratio = [out[0] for out in outputs], outputs[0][1]
            else:
                img, ratio = image, 1.0
        else:
            batch_size = 1
            if self.use_preprocess:
                img, ratio = preprocess(image, (self.input_height, self.input_width), self.pad, self.normal, self.mean,
                                        self.std, self.swap)
            else:
                img, ratio = image, 1.0
        print("preprocess: ", time.time() - s)

        s = time.time()
        self.infer(img)
        print("infer: ", time.time() - s)

        assert self.det_output.shape[1] == (4 + len(self.class_names)), "infer det output shape is not match"

        s = time.time()
        for i in range(batch_size):
            dets, det_scores, det_labels = [], [], []
            boxes = postprocess(self.det_output[i].T, score_thr=self.confidence_thresh, nms_thr=self.nms_thresh,
                                num_classes=len(self.class_names))
            for box, score, label in zip(boxes[:, :4], boxes[:, 4], boxes[:, 5]):
                x1, y1, x2, y2 = box[0] / ratio, box[1] / ratio, box[2] / ratio, box[3] / ratio
                dets.append([max(int(x1), 0), max(int(y1), 0), max(int(x2), 0), max(int(y2), 0)])
                det_scores.append(float(score))
                det_labels.append(int(label))

            total_dets.append(dets)
            total_scores.append(det_scores)
            total_labels.append(det_labels)
        print("postprocess: ", time.time() - s)

        return total_dets, total_scores, total_labels

    def show(self, image, dets, det_scores, det_labels):
        if dets is None or len(dets) == 0:
            return image
        for det, score, label in zip(dets, det_scores, det_labels):
            x1, y1, x2, y2 = det
            cv2.rectangle(image, (x1, y1), (x2, y2), color=(255, 255, 0), thickness=2)
            print(self.class_names[label], score)
            cv2.putText(image, '%s(%.2f)' % (self.class_names[label], score),
                        ((x1 + x2) // 2, (y1 + y2) // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0),
                        thickness=2)

        return image
