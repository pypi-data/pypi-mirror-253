from faceboxes.faceboxes import FaceBoxes
from faceboxes.helper import postprocess_faceboxes
import torch
import cv2
import numpy as np
from utils import resize_images, ensure_directory_exists


class FaceboxDetector:
    def __init__(self):
        facebox_pth = 'faceboxes/FaceBoxes.pth'  # checkpoint for face detector
        detector = FaceBoxes(phase='test', size=None, num_classes=2)
        detector = self.load_model(detector, facebox_pth)
        self.detector = detector.to('cuda:0')
        self.threshold = 0.09

    def load_model(self, model, pretrained_path):
        device = torch.cuda.current_device()
        pretrained_dict = torch.load(pretrained_path, map_location=lambda storage, loc: storage.cuda(device))
        if "state_dict" in pretrained_dict.keys():
            pretrained_dict = self.remove_prefix(pretrained_dict['state_dict'], 'module.')
        else:
            pretrained_dict = self.remove_prefix(pretrained_dict, 'module.')
        model.load_state_dict(pretrained_dict, strict=False)
        return model

    @staticmethod
    def remove_prefix(state_dict, prefix):
        # Old style model is stored with all names of parameters sharing common prefix 'module.'
        f = lambda x: x.split(prefix, 1)[-1] if x.startswith(prefix) else x
        return {f(key): value for key, value in state_dict.items()}

    @staticmethod
    def _pre_processing_faceboxes(image):
        image = resize_images(image, 512)  # 512 worked pretty well for Kitti images
        image = [(cv2.cvtColor(element[0], cv2.COLOR_BGR2RGB), *element[1:]) for element in image]
        image = [(element[0].transpose(2, 0, 1), *element[1:]) for element in image]
        image = [(np.float32(element[0]), *element[1:]) for element in image]
        image = [(torch.from_numpy(element[0]).unsqueeze(0).to(torch.device("cuda")), *element[1:]) for element in
                 image]
        image = [(element[0].to(torch.device("cuda")), *element[1:]) for element in image]
        return image

    def get_bbox_detection(self, image):
        results_list = []
        pre_image = self._pre_processing_faceboxes(image)
        for img in pre_image:
            faceboxes_loc, faceboxes_score = self.detector(img[0])
            result_tuple = (faceboxes_loc, faceboxes_score, img[1], img[2], img[3], img[4])
            results_list.append(result_tuple)
        return results_list, pre_image

    def post_processing(self, results_list, pre_image):
        output = []
        for result, input_image in zip(results_list, pre_image):
            boxes = postprocess_faceboxes(result[0], result[1], input_image[0].shape, self.threshold)
            if len(boxes) is not 0:
                x1, y1, x2, y2, _ = boxes[0]
                # Clamping the values to ensure they are non-negative
                y1 = max(0, int(y1))
                y2 = max(0, int(y2))
                x1 = max(0, int(x1))
                x2 = max(0, int(x2))
                face = input_image[0][0][:, int(y1):int(y2), int(x1):int(x2)]
                face = [face.permute(1, 2, 0)]
                box = [int(value) for value in boxes[:, :4][0].tolist()]
            else:
                face = None
                box = None

            output.append([[face], [[box]], boxes[:, 4], *result[2:]])
        return output

    @staticmethod
    def visualize_face_detection(image_rgb, detected_faces, detected_ped_boxes, output_path, counter):
        image_rgb_copy = np.copy(image_rgb)  # copy to avoid changing image outside this function (ndarray->mutable)
        # Plot bounding boxes
        for index, (faces, ped) in enumerate(zip(detected_faces, detected_ped_boxes)):
            if faces[1].nelement() != 0:
                face_x1, face_y1, face_x2, face_y2 = faces[0][0][0]
                ped_x1, ped_y1, ped_x2, ped_y2 = ped
                new_x1 = ped_x1 + face_x1 * faces[5]
                new_x2 = ped_x1 + face_x2 * faces[5]
                new_y1 = ped_y1 + face_y1 * faces[4]
                new_y2 = ped_y1 + face_y2 * faces[4]

                cv2.rectangle(image_rgb_copy, (int(new_x1.cpu().detach().numpy()), int(new_y1.cpu().detach().numpy())),
                              (int(new_x2.cpu().detach().numpy()), int(new_y2.cpu().detach().numpy())), (0, 255, 0), 2)
            else:
                continue

        image_copy = cv2.cvtColor(image_rgb_copy, cv2.COLOR_RGB2BGR)
        ensure_directory_exists(output_path + '/Pedestrian/')
        save_path = output_path + '/Pedestrian/' + str(counter) + '.png'
        cv2.imwrite(save_path, image_copy)
