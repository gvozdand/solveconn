import torch.nn as nn
import torch


class nn_model(nn.Module):

    def __init__(self, input_dim, hidden_layers: list, output_dim):

        self.input_dim = input_dim
        self.hidden_layers = hidden_layers
        self.output_dim = output_dim

        layers = []
        prev_dim = None

        for counter, dim in enumerate(self.hidden_layers):
    
            if counter != 0:
                layers.append(nn.Linear(prev_dim, dim))
                layers.append(nn.ReLU())
            else:
                layers.append(nn.Linear(input_dim, dim))
                layers.append(nn.ReLU())

        
            prev_dim = dim
        
        layers.append(prev_dim, self.output_dim)


        self.model = nn.Sequential(*layers)



    def forward(self, x):
        return self.model(x)


