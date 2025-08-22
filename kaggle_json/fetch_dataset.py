import kaggle



import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Step 1: Make sure the folder exists
os.makedirs('data/raw', exist_ok=True)

# Step 2: Authenticate Kaggle
api = KaggleApi()
api.authenticate()

# Step 3: Download and unzip dataset
handle = "kazanova/sentiment140"
api.dataset_download_files(handle, path='data/raw', unzip=True)

# Step 4: Find the CSV (automatically)
csv_path = None
for root, dirs, files in os.walk('data/raw'):
    if 'training.1600000.processed.noemoticon.csv' in files:
        csv_path = os.path.join(root, 'training.1600000.processed.noemoticon.csv')
        print("Found CSV at:", csv_path)
        break

# Step 5: Load into pandas
import pandas as pd
dataset = pd.read_csv(csv_path, encoding='latin-1')
print(dataset.head())
