from .models.llm import load_llm
from .models.vision import load_vision_encoder
from .projector import VisionToLLMProjector

class Pipeline:
    def __init__(self, llm_name, vision_name):
        self.llm = load_llm(llm_name)
        self.vision = load_vision_encoder(vision_name)
        self.projector = VisionToLLMProjector(
            vision_dim=self.vision.output_dim,
            llm_dim=self.llm.hidden_size
        )

    def infer(self, image_path, prompt):
        vision_embeds = self.vision.encode(image_path)
        projected = self.projector(vision_embeds)
        return self.llm.generate(prompt, context=projected)
