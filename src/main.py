import os
import torch
import numpy as np
import pandas as pd
import pretrainedmodels
import torch.nn as nn

class SEResNext50_32x4d(nn.Module):
    def __init__(self, pretrained='imagenet'):
        super(SEResNext50_32x4d, self).__init__()
        self.model = pretrainedmodels._dict_['se_resnext50_32x4d'](pretrained = pretrained)
        self.out = nn.Linear(2048,1)
    def forward(self, image):
        bs, _, _, _ = image.shape
        x = self.model.features(image)
        x = F.
