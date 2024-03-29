import torch.nn as nn
import torch

class Embedding(nn.Module):
    # compute word embedding
    def __init__(self, d_model, vocab):

        super(Embedding,self).__init__()
        self.embedding = nn.Embedding(vocab,d_model)
        self.d_model = d_model


    def forward(self, x):
        return self.embedding(x)*torch.sqrt(self.d_model)
