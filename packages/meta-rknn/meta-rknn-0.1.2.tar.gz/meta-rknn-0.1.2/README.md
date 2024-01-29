# metarknn

metarknn部署通用框架

## 1、安装最新版 meta-cv

    pip install meta-cv

## 2、安装最新版 meta-rknn

    pip install meta-rknn

## 3、图像分类示例（参考[classification_demo.py](classification_demo.py)代码）

    import cv2, platform
    import metarknn as m
    
    Classification = m.Classification

    y = Classification(model_path='models/mixnet_xl_bs24_2.rknn',
                       input_width=224,
                       input_height=224,
                       use_preprocess=True,
                       class_names=classnames,
                       device_id=0)
    
    batch_size = 24
    img = cv2.imread('models/bottle.jpg')
    img_list = [img[:, :, ::-1]] * batch_size if batch_size > 1 else img[:, :, ::-1]
    _dets, _scores, _labels = y.predict(img_list)

    # 显示
    y.show(img, _dets, _scores, _labels)
    cv2.imwrite("models/bottle.png", img)

## 4、目标检测示例（参考[detection_demo.py](detection_demo.py)代码）

    import cv2, platform
    import metarknn as m

    Detection = m.Detection

    y = Detection(model_path='models/yolov8m.rknn',
                  input_width=640,
                  input_height=480,
                  use_preprocess=True,
                  pad=True,
                  confidence_thresh=0.5,
                  nms_thresh=0.3,
                  class_names=classnames,
                  device_id=0)
    
    batch_size = 1
    img = cv2.imread('models/bus.jpg')
    img_list = [img[:, :, ::-1]] * batch_size if batch_size > 1 else img[:, :, ::-1]
    _dets, _scores, _labels = y.predict(img_list)
    
    # 显示
    y.show(img, _dets[-1], _scores[-1], _labels[-1])
    cv2.imwrite("models/bus.png", img)

## 5、实例分割示例（参考[segment_demo.py](segment_demo.py)代码）

    import platform, cv2
    import metarknn as m

    Segment = m.Segment

    y = Segment(model_path='models/yolov8m-seg.rknn',
                input_width=640,
                input_height=480,
                use_preprocess=True,
                pad=True,
                confidence_thresh=0.5,
                nms_thresh=0.3,
                class_names=classnames,
                device_id=0)
    
    batch_size = 1
    img = cv2.imread('models/bus.jpg')
    img_list = [img[:, :, ::-1]] * batch_size if batch_size > 1 else img[:, :, ::-1]
    _dets, _scores, _labels = y.predict(img_list)
    
    # 显示
    y.show(img, _dets[-1], _scores[-1], _labels[-1])
    cv2.imwrite("models/bus.png", img)

## 6、模型转换与量化（本地运行）

    import metarknn as m
    
    Quantization = m.Quantization

    q = Quantization(model_path，    # onnx模型路径
                     dataset,   # dataset文件路径
                     mean=[[0, 0, 0]],
                     std=[[255, 255, 255]],
                     batch_size=1)   # 定义模型输出层

    if is_hybrid:   # 是否混合量化
        self.model = q.hybrid_convert()
    else:   # 非混合量化（是否int8量化）
        self.model = q.convert(quantize)
