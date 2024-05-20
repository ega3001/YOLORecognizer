import io

import PIL.Image
import numpy as np
from ultralytics import YOLO


class YoloRecognizer():
    def __init__(self, model_path: str = '', device: str = "cpu", classes: list = []):
        self._filterClasses = classes
        self._predictor = YOLO(model_path)
        self._predictor.to(device)
        self._classes = self._predictor.names

    def _prepare_result(self, instances):
        scores = instances.boxes.conf.tolist()
        pred_classes = instances.boxes.cls.tolist()
        pred_boxes = instances.boxes.xyxy.tolist()

        result = []
        for i, recognized in enumerate(pred_classes):
            if self._filterClasses and self._classes[recognized] not in self._filterClasses:
                continue
            obj = {
                self._classes[recognized]: {
                    "percent": scores[i],
                    "bounds": pred_boxes[i]
                }
            }
            result.append(obj)

        return result

    def score(self, image_buffer: bytes):
        image = PIL.Image.open(io.BytesIO(image_buffer)).convert("RGB")
        open_cv_image = np.array(image)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        # make prediction
        result = self._predictor(open_cv_image)

        return self._prepare_result(result[0])
