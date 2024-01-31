import numpy as np
import torch
from torchvision.ops import nms

from faceboxes.box_utils import decode
from faceboxes.config import cfg
from faceboxes.prior_box import PriorBox


def postprocess_faceboxes(loc, conf, shape, thres):
    priorbox = PriorBox(cfg, image_size=(shape[2], shape[3]))  # height, width
    priors = priorbox.forward()
    priors = priors.to(torch.device("cuda"))
    prior_data = priors.data
    boxes = decode(loc.data.squeeze(0), prior_data, cfg['variance'])

    scale = torch.Tensor([shape[3], shape[2], shape[3], shape[2]]).to(torch.device("cuda"))
    boxes = boxes * scale / 1.0
    #boxes = boxes.cpu()
    scores = conf.squeeze(0)[:, 1]

    # Ignore low scores
    inds = torch.where(scores > thres)[0]
    boxes = boxes[inds]
    scores = scores[inds]

    # Keep top-K before NMS
    order = torch.argsort(scores, descending=True)[:10]
    boxes = boxes[order]
    scores = scores[order]

    # do NMS
    keep_indices = nms(boxes, scores, 0.5)
    expanded_scores = scores.unsqueeze(1)

    # Concatenate 'boxes' and 'expanded_scores' along the second dimension
    dets = torch.cat((boxes, expanded_scores), dim=1).to(torch.float32)

    # dets = np.hstack((boxes, scores[:, np.newaxis])).astype(np.float32, copy=False)
    dets = dets[keep_indices, :]

    # keep top-K faster NMS
    # dets = dets[:5, :]
    return dets
