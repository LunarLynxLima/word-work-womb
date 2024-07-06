import json
from sklearn.model_selection import train_test_split

def load_dataset(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

def save_dataset(data, json_path):
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

def split_dataset(data, test_size=0.1, random_state=42):
    train_data, val_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, val_data

json_path = 'train_file_project.json'
data = load_dataset(json_path)
    
train_data, val_data = split_dataset(data, test_size=0.1 , random_state=1)

save_dataset(train_data, 'train_file.json')
save_dataset(val_data, 'val_file.json')
print("Datasets saved: train_file.json and val_file.json")
