import torch
from torch.utils.data import DataLoader
from diffusers import DDPMScheduler
import torch.nn.functional as F

class StableDiffusionTrainer:
    def __init__(self, unet, vae, text_encoder, dataset, batch_size=1):
        self.unet = unet
        self.vae = vae
        self.text_encoder = text_encoder
        self.noise_scheduler = DDPMScheduler()
        self.dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        self.optimizer = torch.optim.AdamW(self.unet.parameters(), lr=1e-5)
        
    def train_step(self, batch):
        images = batch['image']
        captions = batch['caption']
        
        # Encode text
        text_embeddings = self.text_encoder.encode(captions)
        
        # Encode images to latent space
        latents = self.vae.encode(images)
        
        # Add noise to latents
        noise = torch.randn_like(latents)
        timesteps = torch.randint(0, self.noise_scheduler.num_train_timesteps, (latents.shape[0],))
        noisy_latents = self.noise_scheduler.add_noise(latents, noise, timesteps)
        
        # Predict noise
        noise_pred = self.unet(noisy_latents, timesteps, text_embeddings)
        
        # Calculate loss
        loss = F.mse_loss(noise_pred, noise)
        
        # Update model
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        return loss.item()
