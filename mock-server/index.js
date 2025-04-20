// index.js
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.send('🎉 Hello from the mock server!');
});

app.post('/generate-image', (req, res) => {
  const { prompt } = req.body;
  console.log(`Received prompt: ${prompt}`);

  res.json({
    imageUrl: 'https://picsum.photos/512/512', // fake image placeholder
  });
});

app.listen(5050, () => {
  console.log('Mock server running on http://localhost:5050');
});
