import torch
import torch.nn.functional as F
import torch.nn as nn
from IPython import embed


class UKGE_PSL_Loss(nn.Module):
    """Loss of UKGE with PSL
    """

    def __init__(self, args, model):
        super(UKGE_PSL_Loss, self).__init__()
        self.args = args
        self.model = model

    def forward(self, pos_score, neg_score, PSL_score, pos_sample, neg_sample, PSL_sample):
        confidence = pos_sample[:, 3]  # l_pos
        confidence_2 = neg_sample[:, 3] # l_neg
        confidence_3 = PSL_sample[:, 3] # 拿到每个PSL三元组的置信度

        pos_score = pos_score.squeeze()
        neg_score = neg_score.squeeze()
        PSL_score = PSL_score.squeeze()

        loss_1 = torch.sum((pos_score - confidence) ** 2)
        # loss_2 = torch.sum((confidence_3 - PSL_score) ** 2)
        tmp = torch.clamp((confidence_3 - PSL_score), min=0)
        loss_2 = 0.2 * sum(tmp**2) #TODO 这里应该根据不同规则有修改
        loss_3 = torch.sum(neg_score ** 2)
        # loss_3 = torch.sum()
        pos_neg_ratio = len(confidence)/len(confidence_3)

        loss = loss_1 + loss_2 + loss_3 / neg_score.shape[1]#TODO 暂时先考虑直接乘3，具体还需要后续大规模修改
        return loss
