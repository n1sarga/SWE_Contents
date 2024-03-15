import os
import pandas as pd

df = pd.read_csv('validation.csv')

batch_size = 10000
total_batches = len(df) // batch_size + 1 if len(df) % batch_size != 0 else len(df) // batch_size

output_dir = 'C:\\Users\\nextn\\412 - Test\\Datasets\\val_split'
os.makedirs(output_dir, exist_ok=True)

for i in range(total_batches):
    start_idx = i * batch_size
    end_idx = min((i + 1) * batch_size, len(df))
    batch = df[start_idx:end_idx]
    batch.to_csv(os.path.join(output_dir, f'validation_{i+1}.csv'), index=False)