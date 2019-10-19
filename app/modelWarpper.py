import numpy as np
import torch
from torch import nn
from torchvision import transforms, models
from PIL import Image
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load() : 
    model = models.resnet50()
    model.fc = nn.Sequential(nn.Linear(2048, 512),
                                    nn.ReLU(),
                                    nn.Dropout(0.2),
                                    nn.Linear(512, 4),
                                    nn.LogSoftmax(dim=1))
    model=torch.load('app/models/modelfull',map_location=lambda storage, loc: storage)
    model.eval()
    return model

classes = { 0:"Antedonidae", 1: "Funiculina Virgulania", 2 : "None", 3 : 'Updown'}

def predict_image(model,image):
    test_transforms = transforms.Compose([transforms.Resize(224),
                                        transforms.ToTensor(),
                                        ])
    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = image_tensor
    input = input.to(device)
    output = model(input)
    index = output.data.cpu().numpy().argmax()
    return classes[index]


