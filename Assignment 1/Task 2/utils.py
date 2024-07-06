import torch
import cv2
import glob

class Linear:
    def __init__(self, input_size, output_size):
        self.weights = torch.randn(input_size, output_size) - 0.5
        self.bias = torch.randn(output_size) - 0.5
        self.input_size = input_size
        self.output_size = output_size
        self.x = None

    def forward(self, x):
        self.x = x
        y = torch.mm(self.x, self.weights) + self.bias
        return y
    
    def backward(self, grad):
        grad_x = grad @ self.weights.t()
        grad_weights = self.x.t() @ grad_x
        grad_bias = grad_x.sum(0)
        self.update(grad_weights, grad_bias, 0.001)
        return grad_x
    
    def update(self, grad_weights, grad_bias, learning_rate):
        self.weights -= learning_rate * grad_weights
        self.bias -= learning_rate * grad_bias
    
class ReLU:
    def __init__(self):
        self.x = None

    def forward(self, x):
        self.x = x
        return torch.max(x, torch.zeros_like(x))
    
    def backward(self, grad):
        dz = torch.zeros_like(self.x)
        dz[self.x > 0] = 1
        return grad * dz
    
class sigmoid:
    def __init__(self):
        self.x = None

    def forward(self, x):
        self.x = x
        return 1 / (1 + torch.exp(-x))
    
    def backward(self, grad):
        return grad * (1 - 1 / (1 + torch.exp(-self.x))) * 1 / (1 + torch.exp(-self.x))
    
class Loss:
    def forward(self, y_pred, y_true):
        # compute cross entropy loss
        # print(y_pred, y_true)
        esp = 1e-6
        return -torch.sum(y_true * torch.log(y_pred+esp)) / y_true.shape[0]
    
    def backward(self, y_pred, y_true):
        # compute gradient of cross entropy loss
        return (y_pred - y_true) / y_true.shape[0]
    
class MNISTDataset:
    def __init__(self, training=True):
        if training:
            self.data_path = 'MNIST_DATASET/trainingSet/trainingSet/'
        else:
            self.data_path = 'MNIST_DATASET/testSet/'

        class_path = glob.glob(self.data_path + '*')
        self.data = []
        for path in class_path:
            label = int(path.split('/')[-1])
            images = glob.glob(path + '/*.jpg')
            
            for image in images:
                self.data.append([image, label])
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        img_path, label = self.data[idx]
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_tensor = torch.from_numpy(img).unsqueeze(0).float()
        return img_tensor, label
    
class MNISTDataLoader:
    def __init__(self, dataset, batch_size=128):
        self.dataset = dataset
        self.batch_size = batch_size

    def __iter__(self):
        self.iter = 0
        return self
    
    def __next__(self):
        if self.iter >= len(self.dataset):
            raise StopIteration
        images = []
        labels = []

        for i in range(self.batch_size):
            if self.iter >= len(self.dataset):
                break
            image, label = self.dataset[self.iter]
            images.append(image)
            labels.append(label)
            self.iter += 1


        return torch.stack(images), torch.tensor(labels)
    
    def __len__(self):
        return len(self.dataset) // self.batch_size

    