from transformers import CLIPTokenizer, CLIPTextModel
import torch

class CLIPTextEncoder:
    def __init__(self):
        self.tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")
        self.text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-base-patch32")
        
    def encode(self, text):
        # Tokenize and encode text
        tokens = self.tokenizer(
            text,
            padding="max_length",
            max_length=self.tokenizer.model_max_length,
            truncation=True,
            return_tensors="pt"
        )
        
        # Get text embeddings
        with torch.no_grad():
            text_embeddings = self.text_encoder(tokens.input_ids)[0]
            
        return text_embeddings
