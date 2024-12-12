import Player
import math
import random
import neuralnet as nn

class GeneticAlgorithm():
    def __init__(self):
        self.best = Player.Player(nn.NeuralNetwork(5,5,4,3))
        self.doodler = []
        self.bestFitness = 0

    def populate(self, total, bestBrain):
        '''Create a batch of doodles based on the best doodle'''
        if (bestBrain is None):
            for i in range(total):
                self.doodler.append(Player.Player(nn.NeuralNetwork(5,5,4,3)))
        else:
            for i in range(total):
                self.doodler.append(Player.Player(bestBrain))
        return self.doodler

    def nextGeneration(self, total, array):
        '''Create the next generation of doodles'''
        # Find the doodle with highest fitness before cloning it
        self.bestOne(array)
        self.populate(1, self.best.brain)

        # Clone the best one to be mutated
        clonedBest = self.best.clone()
        clonedBest.fitness = self.bestFitness
        array.append(clonedBest)

        # create 250 doodles with slightly mutated weights/biases OR previous best
        for p in range(total - 1):
            parent = self.selectOne(array)
            self.populate(1, parent)
        array.clear()

    def selectOne(self, array):
        '''Select a random doodle out of the array and mutate it'''
        rand = random.randint(1,len(array)-1)
        array[rand].brain.mutate(0.1)
        return array[rand].brain

    def bestOne(self, array):
        '''Select the best one of the generation and save it'''
        max = 0
        # create a base doodle with fitness 0 to initialize
        currentBest = Player.Player(nn.NeuralNetwork(5,5,4,3))

        # update the best doodle if they exist, based on fitness
        for b in array:
            if (b.fitness >= max):
                max = b.fitness
                currentBest = b
        
        # if current best from the generation is better than all-time best
        if (currentBest.fitness >= self.bestFitness):
            # clone the current best player and update best fitness
            self.best = currentBest.clone()
            self.best.fitness = currentBest.fitness
            self.bestFitness = currentBest.fitness
