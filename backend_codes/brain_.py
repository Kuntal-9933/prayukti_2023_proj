import torch.nn as nn

class Neural_Network():
    def __init__(self,input_layer,hidden_layer,output_layer):
        super(Neural_Network,self).__init__()
        self.layer_1=nn.Linear(input_layer,hidden_layer)
        self.layer_2=nn.Linear(hidden_layer,hidden_layer)
        self.layer_3=nn.Linear(hidden_layer,output_layer)
        self.relu=nn.ReLU()

    def forward_pass(self,x):
       out=self.layer_1(x)
       out=self.relu(out)
       out=self.layer_2(out)
       out=self.relu(out)
       out=self.layer_3(out)
       out=self.relu(out) 
       return out



