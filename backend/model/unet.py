from diffusers import UNet2DConditionModel
import torch

class UNet:
    def __init__(self):
        self.unet = UNet2DConditionModel.from_pretrained(
            "CompVis/stable-diffusion-v1-4",
            subfolder="unet"
        )
        
    def forward(self, latents, timesteps, text_embeddings):
        return self.unet(
            latents,
            timesteps,
            encoder_hidden_states=text_embeddings
        ).sample
