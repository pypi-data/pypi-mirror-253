import cv2
import numpy as np
import torch
from standup_face_recognition2.facenet_pytorch import MTCNN
from standup_face_recognition2.utils import resize_images
from utils import ensure_directory_exists


class MTCNN_detector:
    def __init__(self):
        self.detector = MTCNN(thresholds=[0.2, 0.2, 0.2], keep_all=True, device='cuda', just_the_first_box=True).eval()
        self.detector = self.detector.cuda()

    @staticmethod
    def _pre_processing_mtcnn(image):
        image = resize_images(image, 128)  # 128 worked pretty well for Kitti images
        image = [(np.float32(element[0]), *element[1:]) for element in image]
        image = [(torch.from_numpy(element[0]).unsqueeze(0).to(torch.device("cuda")), *element[1:]) for element in
                 image]
        image = [(element[0].to(torch.device("cuda")), *element[1:]) for element in image]
        return image

    def get_bbox_detection(self, image):
        self.results_list = []
        input_img = self._pre_processing_mtcnn(image)
        for img in input_img:
            faces, _, box, _, probs = self.detector(img[0])
            result_list_single = [faces, box, probs, *img[1:]]
            self.results_list.append(result_list_single)
        return self.results_list

    @staticmethod
    def visualize_face_detection(frame, detected_faces, detected_ped_boxes, output_path, counter):

        # Plot bounding boxes
        for index, (faces, ped) in enumerate(zip(detected_faces, detected_ped_boxes)):
            if faces[2] is not None:
                face_x1, face_y1, face_x2, face_y2 = faces[1][0][0]
                ped_x1, ped_y1, ped_x2, ped_y2 = ped
                new_x1 = ped_x1 + face_x1 * faces[6]
                new_x2 = ped_x1 + face_x2 * faces[6]
                new_y1 = ped_y1 + face_y1 * faces[5]
                new_y2 = ped_y1 + face_y2 * faces[5]

                cv2.rectangle(frame, (round(new_x1), round(new_y1)), (round(new_x2), round(new_y2)), (0, 255, 0), 2)
            else:
                continue

        image_copy = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        ensure_directory_exists(output_path + '/Pedestrian/')
        save_path = output_path + '/Pedestrian/' + str(counter) + '.png'
        cv2.imwrite(save_path, image_copy)
