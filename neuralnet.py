import numpy as np
import random

class NeuralNetwork():

    def __init__(self, in_nodes, hid_nodes, hid_nodes2, out_nodes):
        '''Initialize with random weights and biases, as well as layer sizes'''
        self.input_nodes = in_nodes
        self.hidden_nodes = hid_nodes
        self.hidden_nodes2 = hid_nodes2
        self.output_nodes = out_nodes
        self.weights1 = 2* np.random.random((self.input_nodes, self.hidden_nodes)) -1
        self.weights2 = 2* np.random.random((self.hidden_nodes,self.hidden_nodes2)) -1
        self.weights3 = 2* np.random.random((self.hidden_nodes2,self.output_nodes)) -1
        self.bias1 = 2* np.random.random((self.hidden_nodes)) -1
        self.bias2 = 2* np.random.random((self.hidden_nodes2)) -1
        self.bias3 = 2* np.random.random((self.output_nodes)) -1

    def relu(self, x):
        '''ReLU activation function returns positive number or 0'''
        return np.maximum(0,x)
    
    def feedForward(self, inputs):
        '''Convert inputs to ouput percentages'''
        inputs = np.asarray(inputs)
        hidden = self.relu(np.dot(inputs, self.weights1)+ self.bias1) # 5 input neurons to 4 neurons
        hidden2 = self.relu(np.dot(hidden, self.weights2)+ self.bias2) # 4 neurons to 4 neurons
        output = self.relu(np.dot(hidden2, self.weights3)+ self.bias3) # 4 neurons to 3 neurons
        return output
        
    def mutate(self, rate):
        '''Mutate current weights by a certain degree'''
        def mutation (val):
            # use a gaussian distribution to randomly change weights
            if (np.random.random(1) < rate):
                rand = random.gauss(0, 0.1) + val
                if (rand > 1):
                    rand = 1
                elif (rand < -1):
                    rand =-1
                return rand
            else:
                return val
        vmutate = np.vectorize(mutation) # allows vmutate to be used like a numpy function
        self.weights1 = vmutate(self.weights1)
        self.weights2 = vmutate(self.weights2)
        self.weights3 = vmutate(self.weights3)
        self.bias1 = vmutate(self.bias1)
        self.bias2 = vmutate(self.bias2)
        self.bias3 = vmutate(self.bias3)
    
    def clone(self):
        '''creates a copy of the neural network before manually overriding the random weights from initialization with weights currently in use'''
        cloneBrain = NeuralNetwork(self.input_nodes, self.hidden_nodes, self.hidden_nodes2, self.output_nodes)
        cloneBrain.weights1 = self.weights1
        cloneBrain.weights2 = self.weights2
        cloneBrain.weights3 = self.weights3
        cloneBrain.bias1 = self.bias1
        cloneBrain.bias2 = self.bias2
        cloneBrain.bias3 = self.bias3
        
        return cloneBrain
    
