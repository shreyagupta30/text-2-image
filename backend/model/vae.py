from diffusers import AutoencoderKL
import torch

class VAE:
    def __init__(self):
        self.vae = AutoencoderKL.from_pretrained(
            "CompVis/stable-diffusion-v1-4",
            subfolder="vae"
        )
        self.vae.eval()  # Set to evaluation mode
        
    def encode(self, images):
        with torch.no_grad():
            latents = self.vae.encode(images).latent_dist.sample()
            latents = latents * self.vae.config.scaling_factor
        return latents
    
    def decode(self, latents):
        latents = latents / self.vae.config.scaling_factor
        with torch.no_grad():
            images = self.vae.decode(latents).sample
        return images
