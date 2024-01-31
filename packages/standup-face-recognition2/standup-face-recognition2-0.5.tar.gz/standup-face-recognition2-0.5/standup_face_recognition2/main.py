import cv2
import argparse
from standup_face_recognition2.MTCNN_detector import MTCNN_detector
from standup_face_recognition2.face_recognition import Siamese
from standup_face_recognition2.utils import imread_templates, resize_images_tensor, show_face, standup_roulette
from standup_face_recognition2.pedestrian_detector import PedestrianDetector
from Facebox_detector import FaceboxDetector


def main():
    parser = argparse.ArgumentParser()

    # Define the command-line arguments
    parser.add_argument("--face-detector", type=str, default='FaceBoxes',
                        help="Path to the folder with images that are to be anonymized.")
    parser.add_argument("--face-recognizer", type=str, default='vgg',
                        help="Path to the folder with images that are to be anonymized.")
    parser.add_argument("--output-path", type=str, help="Path where the blurred images are to be saved.")
    parser.add_argument("--debug-visualize-boxes", type=str, default=False, required=False,
                        help="Visualize person and face bounding boxes.")
    args = parser.parse_args()
    # just needed for creating the team embedding
    # template_dict = imread_templates('/home/timo/pip_installable/Webcam/faces_from_webcam')
    names = ['Timo', 'Nitin', 'Karl', 'Martin', 'Kai', 'Robert', 'Hiep', 'Matthias', 'Bharat']
    order_person = ['Timo', 'Bharat', 'Martin', 'Matthias', 'Kai', 'Robert', 'Nitin', 'Hiep', 'Karl']
    person, direction = standup_roulette(names)
    # Init for face recognition
    face_recognition = Siamese(args)
    # Open a connection to the webcam (0 represents the default camera)
    cap = cv2.VideoCapture(0)
    # For creating a video of the output:
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('/home/timo/face_recognition/output.mp4', fourcc, 20.0, (640, 480))

    # Check if the webcam opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    # Person detection
    pedestrian_detector = PedestrianDetector()
    if 'MTCNN' in args.face_detector:
        # MTCNN face detector
        mtcnn_face_detector = MTCNN_detector()
    else:
        # Facebox face detector
        facebox_face_detector = FaceboxDetector()

    counter = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        counter += 1

        # Check if the frame was successfully captured
        if not ret:
            print("Error: Could not read frame.")
            break

        detected_ped_boxes, detected_labels, cropped_ped_images = pedestrian_detector.detect_pedestrians(frame)
        if args.debug_visualize_boxes:
            pedestrian_detector.visualize_pedestrian_detection(frame, detected_ped_boxes, detected_labels,
                                                               args.output_path, counter)

        if 'MTCNN' in args.face_detector:
            detected_faces = mtcnn_face_detector.get_bbox_detection(cropped_ped_images)
            if args.debug_visualize_boxes:
                mtcnn_face_detector.visualize_face_detection(frame, detected_faces, detected_ped_boxes,
                                                             args.output_path, counter)
        elif 'FaceBoxes' in args.face_detector:
            results_list, pre_image = facebox_face_detector.get_bbox_detection(cropped_ped_images)
            detected_faces = facebox_face_detector.post_processing(results_list, pre_image)
            if args.debug_visualize_boxes:
                facebox_face_detector.visualize_face_detection(frame, detected_faces, detected_ped_boxes,
                                                               args.output_path, counter)
        else:
            raise NotImplementedError('This face detector is not implemented yet')

        detected_faces_resized = []
        for ped_box in detected_faces:
            if ped_box[0][0] is not None:
                resized_faces = resize_images_tensor(ped_box, 128)
                face_det_reg = face_recognition.face_recognition(resized_faces, names)  # template_dict
                detected_faces_resized.append(face_det_reg)
            else:
                continue

        show_face(frame, detected_faces_resized, detected_ped_boxes, person, direction)

        if cv2.waitKey(1) & 0xFF == ord('n'):
            person_ind = order_person.index(person)
            if direction is 'clockwise':
                person = order_person[(person_ind + 1) % len(order_person)]
            else:
                person = order_person[(person_ind - 1) % len(order_person)]

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    # out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
