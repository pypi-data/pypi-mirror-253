# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
import os
import platform
import sys
from pathlib import Path

import numpy as np
import torch

FILE = Path(__file__).resolve()
ROOT = ""

from models.common import DetectMultiBackend
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode


class Yolov5:
    index = 0
    # weights = ROOT / 'runs/train/exp2/weights/bestsmall.pt'  # model path or triton URL
    weights = r'./yolov5s.pt'  # model path or triton URL
    # weights = r'E:\Work\PythonProjects\deep_learning\Yolo_malrio\yolov5-master\runs\train\exp8\weights\bestsmall.pt'  # model path or triton URL
    data=r'E:\PypiPublish\wjf-tools\data',                      # file/dir/URL/glob/screen/0(webcam)
    imgsz = (640, 640)                                  # inference size (height, width)
    conf_thres = 0.25                                   # confidence threshold
    iou_thres = 0.45                                    # NMS IOU threshold
    max_det = 1000                                      # maximum detections per image
    device = 'cpu'                                         # cuda device, i.e. 0 or 0,1,2,3 or cpu
    view_img = True                                     # show results
    save_txt = False                                    # save results to *.txt
    save_conf = False                                   # save confidences in --save-txt labels
    save_crop = False                                   # save cropped prediction boxes
    nosave = False                                      # do not save images/videos
    classes = None                                      # filter by class: --class 0, or --class 0 2 3
    agnostic_nms = False                                # class-agnostic NMS
    augment = False                                     # augmented inference
    visualize = False                                   # visualize features
    update = False                                      # update all models
    project = ROOT / 'runs/detect'                      # save results to project/name
    name = 'exp'                                        # save results to project/name
    exist_ok = False                                    # existing project/name ok, do not increment
    line_thickness = 3                                  # bounding box thickness (pixels)
    hide_labels = False                                 # hide labels
    hide_conf = False                                   # hide confidences
    half = False                                        # use FP16 half-precision inference
    dnn = False                                         # use OpenCV DNN for ONNX inference
    vid_stride = 1                                      # video frame-rate stride

    save_img = False
    # Directories
    save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Load model
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data, fp16=half)
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Dataloader
    bs = 1  # batch_size
    # Run inference
    model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
    seen, windows, dt = 0, [], (Profile(), Profile(), Profile())

    def letterbox(self, im, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True,
                  stride=32):
        # Resize and pad image while meeting stride-multiple constraints
        shape = im.shape[:2]  # current shape [height, width]
        if isinstance(new_shape, int):
            new_shape = (new_shape, new_shape)

        # Scale ratio (new / old)
        r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
        if not scaleup:  # only scale down, do not scale up (for better val mAP)
            r = min(r, 1.0)

        # Compute padding
        ratio = r, r  # width, height ratios
        new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
        dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
        if auto:  # minimum rectangle
            dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
        elif scaleFill:  # stretch
            dw, dh = 0.0, 0.0
            new_unpad = (new_shape[1], new_shape[0])
            ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

        dw /= 2  # divide padding into 2 sides
        dh /= 2

        if shape[::-1] != new_unpad:  # resize
            im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
        top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
        left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
        im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
        return im, ratio, (dw, dh)

    def detect(self, img):
        classid=[]
        scores=[]
        box=[]
        self.index += 1
        path = f'image{self.index}.jpg'
        im0s = img
        im = self.letterbox(im0s, self.imgsz, self.stride, self.pt)[0]  # padded resize
        im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        im = np.ascontiguousarray(im)  # contiguous
        s = f'image: '

        with self.dt[0]:
            im = torch.from_numpy(im).to(self.model.device)
            im = im.half() if self.model.fp16 else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim
        # Inference
        with self.dt[1]:
            visualize = increment_path(self.save_dir / Path(path).stem, mkdir=True) if self.visualize else False
            pred = self.model(im, augment=self.augment, visualize=visualize)
        # NMS
        with self.dt[2]:
            pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, self.classes, self.agnostic_nms, max_det=self.max_det)

        # Process predictions
        for i, det in enumerate(pred):  # per image
            p, im0 = path, im0s.copy()

            p = Path(p)  # to Path
            save_path = str(self.save_dir / p.name)  # im.jpg
            s += '%gx%g ' % im.shape[2:]  # print string
            imc = im0.copy() if self.save_crop else im0  # for save_crop
            annotator = Annotator(im0, line_width=self.line_thickness, example=str(self.names))
            if len(det):
                det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, 5].unique():
                    n = (det[:, 5] == c).sum()  # detections per class
                    s += f"{n} {self.names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    # print("四个坐标",xyxy)
                    temp=[]
                    for xy in xyxy:
                        temp.append(xy.int().cpu().item())
                    box.append(temp)
                    scores.append(conf.int().cpu().item())
                    classid.append(cls.int().cpu().item())



                    if self.save_img or self.save_crop or self.view_img:  # Add bbox to image
                        c = int(cls)  # integer class
                        label = None if self.hide_labels else (self.names[c] if self.hide_conf else f'{self.names[c]} {conf:.2f}')
                        # x_avg = int((xyxy[0].item() + xyxy[2].item()) / 2)
                        # y_avg = int((xyxy[1].item() + xyxy[3].item()) / 2)
                        # xy_position = f'({x_avg}, {y_avg})'
                        # cv2.putText(im0, xy_position, (x_avg, y_avg), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                        annotator.box_label(xyxy, label, color=colors(c, True))
                    if self.save_crop:
                        save_one_box(xyxy, imc, file=self.save_dir / 'crops' / self.names[c] / f'{p.stem}.jpg', BGR=True)
                # print(box,scores,classid)
            # Stream results
            im0 = annotator.result()
            if self.view_img:
                if platform.system() == 'Linux' and p not in self.windows:
                    self.windows.append(p)
                    cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                    cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                # cv2.imshow(str(p), im0)
                cv2.imshow('frame', im0)
                cv2.waitKey(1)  # 1 millisecond
            if self.save_img:
                print(save_path)
                cv2.imwrite(save_path, im0)

        # Print time (inference-only)
        LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{self.dt[1].dt * 1E3:.1f}ms")

        # Print results
        if self.save_txt or self.save_img:
            s = f"\n{len(list(self.save_dir.glob('labels/*.txt')))} labels saved to {self.save_dir / 'labels'}" if self.save_txt else ''
            LOGGER.info(f"Results saved to {colorstr('bold', self.save_dir)}{s}")
        return box, scores, classid,im0
def main():
    yolo = Yolov5()

    # # 打开摄像头
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    if ret:
        box, scores, classid, a = yolo.detect(frame)
        print(box, scores, classid, a)
if __name__ == "__main__":
    yolo=Yolov5()
    # # 开启ip摄像头
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            yolo.detect(frame)
        else:
            break



