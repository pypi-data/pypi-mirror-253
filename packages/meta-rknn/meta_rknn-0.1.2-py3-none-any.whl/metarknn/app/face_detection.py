import platform
import metacv as mc
from ..model_zoo import load_model, run


class FaceDetection(mc.FaceDetection):
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
                 class_names=None,
                 device_id=0):
        super().__init__(model_path,
                         input_width,
                         input_height,
                         use_preprocess,
                         pad,
                         normal,
                         mean,
                         std,
                         swap,
                         confidence_thresh,
                         nms_thresh,
                         class_names)
        self.device_id = device_id
        self.model = None
        self.det_output = None
        if platform.machine() == 'aarch64':
            self.initialize_model()

    def convert_and_load(self,
                         quantize=False,
                         dataset='dataset.txt',
                         is_hybrid=False,
                         output_names=["output0"],
                         mean=[[0, 0, 0]],
                         std=[[255, 255, 255]],
                         batch_size=1):
        from .quantization import Quantization

        q = Quantization(self.model_path.replace('.rknn', '.onnx'),
                         dataset,
                         output_names,
                         mean,
                         std,
                         batch_size)
        if is_hybrid:
            self.model = q.hybrid_convert()
        else:
            self.model = q.convert(quantize)

    def initialize_model(self):
        self.model = load_model(self.model_path, self.device_id)

    def infer(self, image):
        # 由继承类实现模型推理
        outputs = run(image, self.model)
        self.det_output = outputs

    def __del__(self):
        # Release
        self.model.release()
