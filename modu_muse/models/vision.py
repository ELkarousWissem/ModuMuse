from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

class VisionWrapper:
    def __init__(self, model, processor):
        self.model = model
        self.processor = processor
        self.output_dim = model.config.projection_dim

    def encode(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.get_image_features(**inputs)
        return outputs
