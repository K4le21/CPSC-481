import numpy as np
import random


class NeuralNetwork():

    def __init__(self, in_nodes, out_nodes):
        
        self.input_nodes = in_nodes
        self.output_nodes = out_nodes
        self.weights1 = 2* np.random.random((self.input_nodes, self.output_nodes)) -1
        self.bias1 = 2* np.random.random((self.output_nodes)) -1

    # Activation functions
    def relu(self, x):
        #using relu function
        return np.maximum(0,x)
    
    def feedForward(self, inputs):
        inputs = np.asarray(inputs)  # convert inputs into np array
        output = self.relu(np.dot(inputs, self.weights1)+ self.bias1)
        return output
        
    def mutate(self, rate):   
        def mutation (val):
            if (np.random.random(1) < rate):
                rand = random.gauss(0, 0.1) + val
                if (rand > 1):
                    rand = 1
                elif (rand < -1):
                    rand =-1

                return rand
            else:
                return val
        vmutate = np.vectorize(mutation)
        self.weights1 = vmutate(self.weights1)
        self.bias1 = vmutate(self.bias1)
    
    def clone(self):
        # Creates a clone of a neural network before overriding the random weights and biases
        cloneBrain = NeuralNetwork(self.input_nodes, self.output_nodes)
        cloneBrain.weights1 = self.weights1
        cloneBrain.bias1 = self.bias1
        return cloneBrain
    
