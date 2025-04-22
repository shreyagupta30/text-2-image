import React, { useState } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerate = async () => {
    setLoading(true);
    setError('');
    setImageUrl('');

    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });

      const data = await response.json();

      if (response.ok){
        if (data.image) {
          setImageUrl(data.image);
        } else {
          setError('No image returned from server');
        }
      } else{
          setError(data.detail || 'Failed to generate image');
      }
    } catch (err) {
        setError('Error occurred: ' + err.message);
        console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <h1>🖼️ AI Image Generator</h1>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt..."
      />
      <button onClick={handleGenerate} disabled={!prompt || loading}>
        {loading ? 'Generating...' : 'Generate'}
      </button>

      {error && <p className="error">{error}</p>}
      {imageUrl && (
        <div className="image-container">
          <img src={imageUrl} alt="Generated result" />
        </div>
      )}
    </div>
  );
}

export default App;
