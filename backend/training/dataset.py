import torch
from torch.utils.data import Dataset
from PIL import Image
import os

class Flickr8kDataset(Dataset):
    def __init__(self, image_dir, captions_file, transform=None):
        self.image_dir = image_dir
        self.transform = transform
        self.image_captions = {}
        
        # Load captions
        with open(captions_file, 'r') as f:
            for line in f:
                if line.startswith('image'):
                    continue
                parts = line.strip().split(',')
                image_name = parts[0]
                caption = parts[1]
                
                if image_name not in self.image_captions:
                    self.image_captions[image_name] = []
                self.image_captions[image_name].append(caption)
                
        self.images = list(self.image_captions.keys())
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        image_name = self.images[idx]
        image_path = os.path.join(self.image_dir, image_name)
        image = Image.open(image_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
            
        # Randomly select one caption for the image
        caption = self.image_captions[image_name][0]
        
        return {
            'image': image,
            'caption': caption
        }
