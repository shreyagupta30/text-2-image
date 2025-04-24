import React, { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [messages, setMessages] = useState([]);
  const chatRef = useRef(null);

  useEffect(() => {
    setMessages([{ from: 'bot', text: '👋 Welcome! Please enter your prompt.' }]);
  }, []);

  useEffect(() => {
    chatRef.current?.scrollTo({ top: chatRef.current.scrollHeight, behavior: 'smooth' });
  }, [messages]);

  const handleGenerate = async () => {
    if (!prompt.trim()) return;

    setError('');
    setLoading(true);

    const userMsg = { from: 'user', text: prompt };
    const botTyping = { from: 'bot', text: '🤖 Generating your image...' };

    setMessages((prev) => [...prev, userMsg, botTyping]);

    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });

      const data = await response.json();

      if (response.ok && data.image) {
        setMessages((prev) => [
          ...prev.slice(0, -1),
          { from: 'bot', text: '🎉 Here is your image!' },
          { from: 'bot', image: data.image },
          { from: 'bot', text: '💡 Would you like to try another prompt?' }
        ]);
      } else {
        const errMsg = data.detail || '⚠️ No image returned from server';
        setError(errMsg);
        setMessages((prev) => [...prev.slice(0, -1), { from: 'bot', text: errMsg }]);
      }
    } catch (err) {
      const errMsg = '❌ Error: ' + err.message;
      setError(errMsg);
      setMessages((prev) => [...prev.slice(0, -1), { from: 'bot', text: errMsg }]);
    }

    setPrompt('');
    setLoading(false);
  };

  return (
    <div className="App">
      <h1 className="title">💬 AI Image Chatbot</h1>

      <div className="chat-window" ref={chatRef}>
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.from}`}>
            {msg.text && <p>{msg.text}</p>}
            {msg.image && <img src={msg.image} alt="Generated" className="chat-image" />}
          </div>
        ))}
      </div>

      <div className="input-area">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Describe your image idea..."
          disabled={loading}
          rows={3}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              handleGenerate();
            }
          }}
        />
        <button onClick={handleGenerate} disabled={!prompt || loading}>
          {loading ? 'Generating...' : 'Send'}
        </button>
      </div>
    </div>
  );
}

export default App;
