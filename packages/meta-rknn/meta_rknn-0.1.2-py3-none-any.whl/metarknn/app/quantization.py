import os, platform

if platform.machine() == 'aarch64':
    from rknnlite.api import RKNNLite as RKNN
else:
    from rknn.api import RKNN


class Quantization:
    def __init__(self,
                 model_path: str,  # onnx model name
                 dataset_file: str,  # dataset file
                 output_names: list,
                 mean=[[0, 0, 0]],
                 std=[[255, 255, 255]],
                 batch_size=1):
        self.model_path = model_path
        self.dataset_file = dataset_file
        self.output_names = output_names
        self.mean = mean
        self.std = std
        self.batch_size = batch_size

    def hybrid_convert(self, ):
        model = RKNN(verbose=False)
        model.config(mean_values=self.mean, std_values=self.std, target_platform="rk3588")
        ret = model.load_onnx(model=self.model_path, outputs=self.output_names)
        if ret != 0:
            print('Load model failed!')
            exit(ret)

        ret = model.hybrid_quantization_step1(dataset=self.dataset_file, rknn_batch_size=self.batch_size,
                                              proposal=False)
        if ret != 0:
            print('hybrid_quantization_step1 failed!')
            exit(ret)

        ret = model.hybrid_quantization_step2(
            model_input=os.path.basename(self.model_path.replace('.onnx', '.model')),
            data_input=os.path.basename(self.model_path.replace('.onnx', '.data')),
            model_quantization_cfg=os.path.basename(self.model_path.replace('.onnx', '.quantization.cfg')))
        if ret != 0:
            print('hybrid_quantization_step2 failed!')
            exit(ret)

        ret = model.export_rknn(self.model_path.replace('.onnx', '.rknn'))
        if ret != 0:
            print('Export model model failed!')
            exit(ret)

        ret = model.init_runtime()
        if ret != 0:
            print('Init runtime environment failed!')
            exit(ret)

        return model

    def convert(self, quantize=False):
        model = RKNN(verbose=False)
        model.config(mean_values=[[0, 0, 0]], std_values=[[255, 255, 255]], target_platform='rk3588')
        ret = model.load_onnx(model=self.model_path, outputs=self.output_names)
        if ret != 0:
            print('Load model failed!')
            exit(ret)

        ret = model.build(do_quantization=quantize, dataset=self.dataset_file, rknn_batch_size=self.batch_size)
        if ret != 0:
            print('Build model failed!')
            exit(ret)

        ret = model.export_rknn(self.model_path.replace('.onnx', '.rknn'))
        if ret != 0:
            print('Export model model failed!')
            exit(ret)

        ret = model.init_runtime()
        if ret != 0:
            print('Init runtime environment failed!')
            exit(ret)

        return model
