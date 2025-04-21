# Text-to-Image Generation with Stable Diffusion

This project implements a text-to-image generation system using the Stable Diffusion model with FastAPI backend and a web interface.

## 🌟 Features

- Text prompt to image generation using Stable Diffusion
- FastAPI backend with REST API endpoints
- CLIP text encoding for prompt understanding
- VAE for image encoding/decoding
- U-Net architecture for the core diffusion process
- Fine-tuning capabilities using Flickr8k dataset
- Base64 image response format

## 🛠️ Project Structure

```
text-2-image/
├── backend/
│   ├── model/
│   │   ├── clip_tokenizer.py  # CLIP text encoding
│   │   ├── unet.py           # U-Net model
│   │   └── vae.py            # VAE encoder/decoder
│   ├── training/
│   │   ├── dataset.py        # Flickr8k dataset handler
│   │   └── trainer.py        # Training logic
│   ├── api/
│   │   └── main.py          # FastAPI endpoints
│   └── requirements.txt      # Python dependencies
└── mock-server/             # Development mock server
    ├── index.js
    └── package.json
```

## ⚙️ Installation

### Backend Setup

1. Create and activate a virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the FastAPI server:
```bash
uvicorn api.main:app --reload --port 8000
```

### Mock Server Setup (for development)

1. Install Node.js dependencies:
```bash
cd mock-server
npm install
```

2. Start the mock server:
```bash
node index.js
```

## 🚀 API Usage

### Generate Image Endpoint

- **URL**: `/generate`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:
```json
{
    "prompt": "your text description here"
}
```
- **Response**:
```json
{
    "image": "data:image/png;base64,..."
}
```

## 💻 Development

### Model Components

1. **CLIP Text Encoder** (`model/clip_tokenizer.py`)
   - Converts text prompts into embeddings
   - Uses OpenAI's CLIP model

2. **VAE** (`model/vae.py`)
   - Handles image encoding/decoding
   - Manages latent space representations

3. **U-Net** (`model/unet.py`)
   - Core diffusion model
   - Processes latent representations

### Training

1. Prepare your dataset:
```python
from training.dataset import Flickr8kDataset
dataset = Flickr8kDataset(
    image_dir="path/to/images",
    captions_file="path/to/captions.txt"
)
```

2. Initialize trainer:
```python
from training.trainer import StableDiffusionTrainer
trainer = StableDiffusionTrainer(unet, vae, text_encoder, dataset)
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ✨ Acknowledgments

- [Stable Diffusion](https://github.com/CompVis/stable-diffusion) by CompVis
- [Hugging Face Diffusers](https://github.com/huggingface/diffusers)
- [CLIP](https://github.com/openai/CLIP) by OpenAI
- [Flickr8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k) for training

