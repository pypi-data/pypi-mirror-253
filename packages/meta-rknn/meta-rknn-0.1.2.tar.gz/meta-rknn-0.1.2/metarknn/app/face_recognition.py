import cv2
import platform
import numpy as np
from metacv import Face as F
from .face_detection import FaceDetection
from .face_embedding import FaceEmbedding


class FaceRecognition:
    def __init__(self,
                 detection_model_path='models/face_detection.rknn',
                 recognition_model_path='models/face_recognition.rknn',
                 confidence_thresh=0.5,
                 nms_thresh=0.4,
                 class_names=['face'],
                 device_id=0):
        self.detector = FaceDetection(model_path=detection_model_path,
                                      input_width=480,
                                      input_height=640,
                                      use_preprocess=True,
                                      pad=True,
                                      confidence_thresh=confidence_thresh,
                                      nms_thresh=nms_thresh,
                                      class_names=class_names,
                                      device_id=device_id)
        if platform.machine() == 'x86_64':
            self.detector.convert_and_load(quantize=False,  # 是否int8量化
                                           dataset='detection_dataset.txt',  # 量化使用图片路径文件
                                           is_hybrid=True,  # 是否进行混合量化
                                           output_names=None,
                                           mean=[[123.675, 116.28, 103.53]],
                                           std=[[58.395, 57.12, 57.375]],
                                           batch_size=1)
        self.recognizer = FaceEmbedding(model_path=recognition_model_path,
                                        input_width=112,
                                        input_height=112,
                                        use_preprocess=True,
                                        device_id=device_id)
        if platform.machine() == 'x86_64':
            self.recognizer.convert_and_load(quantize=False,  # 是否int8量化
                                             dataset='embedding_dataset.txt',  # 量化使用图片路径文件
                                             is_hybrid=True,  # 是否进行混合量化
                                             output_names=None,
                                             mean=[[127.5, 127.5, 127.5]],
                                             std=[[127.5, 127.5, 127.5]],
                                             batch_size=1)

    def predict(self, image):
        total_faces = []
        total_bboxes, total_scores, total_kpss = self.detector.predict(image)
        for i in range(len(total_bboxes)):
            bboxes, scores, kpss = total_bboxes[i], total_scores[i], total_kpss[i]
            img = image[i] if isinstance(image, list) else image
            faces = []
            for bbox, score, kps in zip(bboxes, scores, kpss):
                face = F(bbox=bbox, kps=np.array(kps), score=score)
                align_img = F.norm_crop(img, face.kps)
                face.embedding = self.recognizer.predict(align_img)
                faces.append(face)
            total_faces.append(faces)

        return total_faces

    @staticmethod
    def show(image, faces):
        for face in faces:
            bbox, score, kps = face.bbox, face.score, face.kps
            x1, y1, x2, y2 = bbox
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            for k in kps:
                cv2.circle(image, (k[0], k[1]), 5, (0, 0, 255), -1)
            cv2.putText(image, '%.2f' % score,
                        ((x1 + x2) // 2, (y1 + y2) // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0),
                        thickness=2)
        return image
