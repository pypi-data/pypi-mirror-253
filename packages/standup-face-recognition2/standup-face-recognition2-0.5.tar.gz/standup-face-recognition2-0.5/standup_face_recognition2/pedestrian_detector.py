import os
import time
import cv2
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn, ssd300_vgg16
from torchvision.transforms import functional as F
from utils import ensure_directory_exists


class PedestrianDetector:
    def __init__(self):
        # Load a pretrained Faster R-CNN model for pedestrian detection
        self.model = fasterrcnn_resnet50_fpn(pretrained=True).cuda()
        # self.model = ssd300_vgg16(pretrained=True)
        self.model.eval()
        self.score_threshold = 0.5

    def detect_pedestrians(self, frame):

        # Convert cv2 image to torch tensor
        input_tensor = F.to_tensor(frame).unsqueeze(0).cuda()
        # start_time = time.time()
        # Forward pass through the model
        with torch.no_grad():
            prediction = self.model(input_tensor)
        # print(f'Prediction time: {time.time() - start_time}')

        # Filter detections based on confidence score
        boxes = prediction[0]['boxes'][prediction[0]['scores'] > self.score_threshold].cpu().numpy()
        labels = prediction[0]['labels'][prediction[0]['scores'] > self.score_threshold].cpu().numpy()

        cropped_images = []
        label_list = []
        box_list = []
        for i, (box, label) in enumerate(zip(boxes, labels)):
            # just process the person label (1)
            if label != 1:
                continue
            # Convert box coordinates to integers
            box = tuple(map(int, box))

            # Crop the image based on the bounding box
            cropped_image = frame[box[1]:box[3], box[0]:box[2]]

            # Save or append the cropped image to the list
            cropped_images.append(cropped_image)
            box_list.append(box)
            label_list.append(label)

        return box_list, label_list, cropped_images

    @staticmethod
    def visualize_pedestrian_detection(image, boxes, labels, output_path, counter):

        for box, label in zip(boxes, labels):
            xmin, ymin, xmax, ymax = box
            cv2.rectangle(image, (round(xmin), round(ymin)), (round(xmax), round(ymax)), (0, 255, 0), 2)

        image_copy = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        ensure_directory_exists(output_path + '/Pedestrian/')
        save_path = output_path + '/Pedestrian/' + str(counter) + '.png'
        cv2.imwrite(save_path, image_copy)

    @staticmethod
    def save_cropped_images(cropped_ped_images, output_path):
        for i, img_array in enumerate(cropped_ped_images):
            # Ensure the array values are in the uint8 range [0, 255]
            img_array = img_array.astype('uint8')

            # Define the file path to save the image
            file_path = os.path.join(output_path + '/cropped_images/', f'image_{i + 1}.png')

            # Save the image using OpenCV
            cv2.imwrite(file_path, cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
