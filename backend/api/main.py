from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from PIL import Image
import io
import base64

from model.clip_tokenizer import CLIPTextEncoder
from model.vae import VAE
from model.unet import UNet
from diffusers import DDPMScheduler

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextPrompt(BaseModel):
    prompt: str

# Initialize models
text_encoder = CLIPTextEncoder()
vae = VAE()
unet = UNet()
noise_scheduler = DDPMScheduler()

@app.post("/generate")
async def generate_image(prompt: TextPrompt):
    try:
        # Encode text
        text_embeddings = text_encoder.encode(prompt.prompt)
        
        # Start from random noise
        latents = torch.randn(
            (1, unet.unet.config.in_channels, 64, 64)
        )
        
        # Denoise
        for t in noise_scheduler.timesteps:
            with torch.no_grad():
                noise_pred = unet.forward(latents, t, text_embeddings)
                latents = noise_scheduler.step(noise_pred, t, latents).prev_sample
        
        # Decode latents to image
        image = vae.decode(latents)
        
        # Convert to PIL Image and then to base64
        image = (image / 2 + 0.5).clamp(0, 1)
        image = image.cpu().permute(0, 2, 3, 1).numpy()[0]
        image = Image.fromarray((image * 255).astype('uint8'))
        
        # Convert to base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return {"image": f"data:image/png;base64,{img_str}"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
