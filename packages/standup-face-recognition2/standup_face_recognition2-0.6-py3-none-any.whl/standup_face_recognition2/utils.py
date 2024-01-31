import numpy as np
import cv2
import os
import torchvision.transforms as transforms
import torch
import random


def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created.")


def standup_roulette(persons):
    # Select a random person from the list
    random_person = random.choice(persons)

    # Select a random direction
    direction = random.choice(['clockwise', 'counterclockwise'])
    return random_person, direction


def resize_images(images, resize_size):
    resized_images = []

    for img in images:
        current_height, current_width, _ = img.shape

        # Calculate the new dimensions to be 5 times divisible by 2
        new_width = int(np.ceil(current_width / 2 ** 5) * 2 ** 5)
        new_height = int(np.ceil(current_height / 2 ** 5) * 2 ** 5)

        # Check if either dimension is smaller than 128
        if new_width < resize_size or new_height < resize_size:
            # Calculate the scaling factor to ensure both dimensions are at least 80
            scaling_factor = max(resize_size / new_width, resize_size / new_height)
            # Upscale both dimensions with the same factor
            new_width = int(new_width * scaling_factor)
            new_height = int(new_height * scaling_factor)

        scaling_factor_width = current_width / new_width
        scaling_factor_height = current_height / new_height

        # Resize the image using OpenCV or any other library of your choice
        resized_img = cv2.resize(img, (new_width, new_height))
        resized_images.append([resized_img, current_height, current_width, scaling_factor_height, scaling_factor_width])

    return resized_images


def resize_images_tensor(images, resize_size):
    resized_images = []
    resized_images_total = []
    for index, img in enumerate(images[0][0]):

        # Convert PyTorch tensor to NumPy array
        img_np = img.cpu().detach().numpy()

        current_height, current_width, _ = img_np.shape

        # Calculate the new dimensions to be 5 times divisible by 2
        new_width = 96  # int(np.ceil(current_width / 2 ** 5) * 2 ** 5)
        new_height = 128  # int(np.ceil(current_height / 2 ** 5) * 2 ** 5)

        # Check if either dimension is smaller than 128
        if new_width < resize_size or new_height < resize_size:
            # Calculate the scaling factor to ensure both dimensions are at least 80
            scaling_factor = max(resize_size / new_width, resize_size / new_height)
            # Upscale both dimensions with the same factor
            new_width = int(new_width * scaling_factor)
            new_height = int(new_height * scaling_factor)

        # Resize the image using OpenCV or any other library of your choice
        try:
            resized_img = cv2.resize(img_np, (new_width, new_height))
        except:
            print("k")

        # Convert the resized image back to a PyTorch tensor
        resized_img_tensor = torch.from_numpy(resized_img).cuda()

        # Append information along with the resized image to the list
        resized_images.append(resized_img_tensor)

    #  scaling factor is not needed for face recognition
    resized_images_total.append(resized_images)
    resized_images_total.append(images[1])  # append box coor
    resized_images_total.append(images[2])  # append score
    resized_images_total.append(images[3])  # append org_height
    resized_images_total.append(images[4])  # append org_width
    resized_images_total.append(images[5])  # append scale
    resized_images_total.append(images[6])  # append scale
    return resized_images_total


def show_face(frame, resized_faces, pedestrian_boxes, start_person, direction):
    for ped_box, ped in zip(resized_faces, pedestrian_boxes):
        # Plot bounding boxes
        for index, faces in enumerate(ped_box[1][0]):
            if faces is not None:
                # Find the person with the highest score per box
                max_key = None
                max_value = float('-inf')

                for d in ped_box[7+index]:
                    # Find the key with the maximum value in the current dictionary
                    current_max_key = max(d, key=d.get)
                    current_max_value = d[current_max_key]

                    # Update the overall maximum key and value if necessary
                    if current_max_value > max_value:
                        max_key = current_max_key
                        max_value = current_max_value

                color = (0, 0, 255)
                text = f"'{max_key}'"
                if start_person is max_key:
                    color = (0, 255, 0)
                    text = f"'{max_key}' + {str(direction)}"

                face_x1, face_y1, face_x2, face_y2 = faces
                ped_x1, ped_y1, ped_x2, ped_y2 = ped
                # do not show faces with a width smaller than 30 px
                if ((ped_x1 + face_x2 * ped_box[6]) - (ped_x1 + face_x1 * ped_box[6])) < 20:
                    continue
                new_x1 = ped_x1 + face_x1 * ped_box[6]
                new_x2 = ped_x1 + face_x2 * ped_box[6]
                new_y1 = ped_y1 + face_y1 * ped_box[5]
                new_y2 = ped_y1 + face_y2 * ped_box[5]

                cv2.rectangle(frame, (round(new_x1), round(new_y1)), (round(new_x2), round(new_y2)), color, 2)
                # cv2.rectangle(frame, (int(new_x1), int(new_y1)), (int(new_x2), int(new_y2)), color, 2)

                cv2.putText(frame, text, (round(new_x1), round(new_y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            else:
                continue

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # out.write(frame)
    cv2.imshow('Webcam output', frame)


def imread_templates(folder_path):
    image_dict = {}
    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # List all files in the folder
        files = os.listdir(folder_path)

        # Filter only files with specific extensions (e.g., '.png', '.jpg')
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # Read each image and append it to the list
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image = resize_images([image], 128)
            image = image[0][0]
            image = transforms.ToTensor()(image).unsqueeze(0).cuda()
            image_name = image_file.split('.')[0]
            if image is not None:
                image_dict[image_name] = image
            else:
                print(f"Failed to read image: {image_path}")
    else:
        print("Folder not found.")
    return image_dict
