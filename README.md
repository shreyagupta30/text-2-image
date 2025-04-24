# Text-to-Image Web App

Generate photorealistic images from natural language prompts using Stable Diffusion v1.4.

## Table of Contents
1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
   - [Backend](#backend)
   - [Frontend](#frontend)
5. [API Reference](#api-reference)
6. [Contributing](#contributing)
7. [License](#license)

## Features
- Text-to-image generation powered by Stable Diffusion v1.4
- FastAPI backend with RESTful endpoints
- React frontend with live image preview
- Base64-encoded image responses
- Health check endpoint

## Tech Stack
**Backend**: Python 3.8+, FastAPI, Hugging Face Diffusers, PyTorch  
**Frontend**: React (JavaScript/ES6+), CSS3

## Project Structure
```
text-2-image/
├── backend/
│   ├── api/
│   │   └── main.py         FastAPI endpoints
│   └── requirements.txt    Python dependencies
└── frontend/
    ├── public/             Static assets
    ├── src/
    │   ├── components/     React components
    │   └── App.js          Main application
    └── package.json        Node.js dependencies
```

## Installation

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm start
```

_Backend:_ http://localhost:8000  
_Frontend:_ http://localhost:3000

## API Reference

### POST /generate
**Request**
```json
{ "prompt": "Your text prompt" }
```
**Response**
```json
{ "image": "data:image/png;base64,..." }
```

### GET /health
**Response**
```json
{ "status": "healthy" }
```

## Contributing
1. Fork the repository
2. Create a branch: `git checkout -b feature/xyz`
3. Commit changes: `git commit -m "feat: describe your changes"`
4. Push branch: `git push origin feature/xyz`
5. Open a Pull Request

## License
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
