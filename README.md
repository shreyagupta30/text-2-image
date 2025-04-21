# Text-to-Image Generation with Stable Diffusion

A web application that generates images from text descriptions using the Stable Diffusion model, featuring a FastAPI backend and React frontend.

## 🌟 Features

- Text-to-image generation using Stable Diffusion v1.4
- FastAPI backend with REST API
- React frontend with real-time image generation
- Base64 image response format
- Health check endpoint

## 🛠️ Project Structure

```
text-2-image/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   └── main.py          # FastAPI endpoints
│   └── requirements.txt      # Python dependencies
└── frontend/
    ├── src/
    │   ├── App.js           # React frontend
    │   └── components/
    ├── public/
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

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm start
```

## 🚀 API Endpoints

### Generate Image
- **URL**: `/generate`
- **Method**: `POST`
- **Body**:
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

### Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Response**:
```json
{
    "status": "healthy"
}
```

## 💻 Technologies Used

- **Backend**:
  - FastAPI
  - Hugging Face Diffusers
  - PyTorch
  - Python 3.8+

- **Frontend**:
  - React
  - JavaScript/ES6
  - CSS3

## 🔧 Requirements

- Python 3.8+
- Node.js 14+
- npm 6+
- 8GB+ RAM recommended
- GPU support (optional but recommended)

## 📝 Environment Variables

None required. The application uses default configurations:
- Backend runs on `http://localhost:8000`
- Frontend runs on `http://localhost:3000`
- Uses Hugging Face's hosted Stable Diffusion v1.4 model

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) by CompVis
- [Hugging Face](https://huggingface.co/) for model hosting
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [React](https://reactjs.org/) for the frontend framework
