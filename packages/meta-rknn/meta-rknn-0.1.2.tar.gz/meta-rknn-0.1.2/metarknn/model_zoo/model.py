import platform
import numpy as np

if platform.machine() == 'aarch64':
    from rknnlite.api import RKNNLite as RKNN
else:
    from rknn.api import RKNN


def load_model(model_path, device_id):
    rknn = RKNN(verbose=False)
    rknn.load_rknn(model_path)
    ret = rknn.init_runtime(core_mask=device_id)
    if ret != 0:
        print('Init runtime environment failed!')
        exit(ret)

    return rknn


def run(images, model):
    input_tensor = np.array(images) if isinstance(images, list) else images[np.newaxis, :, :, :]
    outputs = model.inference(inputs=[input_tensor])

    return outputs
