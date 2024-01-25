import cv2
import time
from ..utils import preprocess, postprocess_2


class FaceDetection:
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
        total_dets, total_scores, total_kpss = [], [], []
        s = time.time()
        if isinstance(image, list):
            batch_size = len(image)
            if self.use_preprocess:
                outputs = [preprocess(im, (self.input_height, self.input_width),
                                      self.pad, self.normal, self.mean, self.std, self.swap) for im in image]
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

        s = time.time()
        for i in range(batch_size):
            dets, det_scores, det_kpss = [], [], []
            boxes, kpss = postprocess_2(self.det_output, (self.input_height, self.input_width), self.confidence_thresh,
                                        self.nms_thresh)
            for box, score, kps in zip(boxes[:, :4], boxes[:, 4], kpss):
                x1, y1, x2, y2 = box[0] / ratio, box[1] / ratio, box[2] / ratio, box[3] / ratio
                dets.append([max(int(x1), 0), max(int(y1), 0), max(int(x2), 0), max(int(y2), 0)])
                det_scores.append(float(score))
                det_kpss.append([(int(k[0] / ratio), int(k[1] / ratio)) for k in kps])

            total_dets.append(dets)
            total_scores.append(det_scores)
            total_kpss.append(det_kpss)
        print("postprocess: ", time.time() - s)

        return total_dets, total_scores, total_kpss

    def show(self, image, dets, det_scores, det_kpss):
        if dets is None or len(dets) == 0:
            return image
        for det, score, kps in zip(dets, det_scores, det_kpss):
            x1, y1, x2, y2 = det
            cv2.rectangle(image, (x1, y1), (x2, y2), color=(255, 255, 0), thickness=2)
            for k in kps:
                cv2.circle(image, (k[0], k[1]), 5, (0, 0, 255), -1)
            print(self.class_names[0], score)
            cv2.putText(image, '%s(%.2f)' % (self.class_names[0], score),
                        ((x1 + x2) // 2, (y1 + y2) // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0),
                        thickness=2)

        return image
