import torch
import os
import torch.nn as nn
from standup_face_recognition2.facenet_pytorch import InceptionResnetV1


class Siamese:
    def __init__(self, args):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        if 'vgg' in args.face_recognizer:
            Siamese_network = InceptionResnetV1(pretrained='vggface2')
            model_path = os.path.join(script_dir, "20180402-114759-vggface2.pt")
            if 'MTCNN' in args.face_detector:
                team_embedding_path = os.path.join(script_dir, "team_embedding_webcam_mtcnn_vgg.pth")
            else:
                team_embedding_path = os.path.join(script_dir, "team_embedding_webcam_faceboxes_vgg.pth")
        else:
            Siamese_network = InceptionResnetV1(pretrained='casia-webface')
            model_path = os.path.join(script_dir, "20180408-102900-casia-webface.pt")
            if 'FaceBoxes' in args.face_detector:
                team_embedding_path = os.path.join(script_dir, "team_embedding_webcam_faceboxes_casia.pth")
            else:
                team_embedding_path = os.path.join(script_dir, "team_embedding_webcam_mtcnn_casia.pth")

        checkpoint = (torch.load(model_path))
        Siamese_network.load_state_dict(checkpoint)
        Siamese_network = Siamese_network.cuda()
        Siamese_network.eval()
        self.Siamese_network = Siamese_network
        self.cos = nn.CosineSimilarity(dim=1, eps=1e-6)
        self.team_embedding = (torch.load(team_embedding_path))

    def face_recognition(self, detected_face, names):  # template

        for det_face in detected_face[0]:
            similarity_list = []
            # embedding_list = []
            embedding1 = self.Siamese_network(det_face.permute(2, 0, 1).unsqueeze(0))
            for index, name in enumerate(names):
            # for index, t in enumerate(template.items()):
                # embedding2 = self.Siamese_network(t[1])
                # embedding_list.append(embedding2)
                cosine_similarity = self.cos(embedding1, self.team_embedding[index]).item()
                similarity_list.append({name: cosine_similarity})
            # torch.save(embedding_list, '/home/timo/pip_installable/standup-face-recognition/standup_face_recognition/team_embedding_webcam_faceboxes_casia.pth')
            detected_face.append(similarity_list)
        return detected_face
