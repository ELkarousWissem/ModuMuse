import torch.nn as nn

class VisionToLLMProjector(nn.Module):
    def __init__(self, vision_dim, llm_dim):
        super().__init__()
        self.proj = nn.Sequential(
            nn.Linear(vision_dim, llm_dim),
            nn.ReLU(),
            nn.Linear(llm_dim, llm_dim)
        )

    def forward(self, vision_embeds):
        return self.proj(vision_embeds)
