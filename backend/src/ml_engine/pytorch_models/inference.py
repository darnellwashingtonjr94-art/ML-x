import torch
import torch.nn as nn

class DummyModel(nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

def run_pytorch_inference(data: list) -> list:
    # In production, load from a saved .pt or .pth file
    model = DummyModel()
    model.eval()
    
    input_tensor = torch.tensor(data, dtype=torch.float32)
    with torch.no_grad():
        output = model(input_tensor)
        
    return output.tolist()
