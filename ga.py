import Player
import pygame
import math
import random
import neuralnet as nn


class GeneticAlgorithm:
    def __init__(self):
        self.best = Player.Player(nn.NeuralNetwork(5, 4, 3))  # All-time best player
        self.doodlers = []  # Current population
        self.best_fitness = 0

    def populate(self, total, best_brain=None):
        """
        Populate the next generation. If `best_brain` is provided, players
        will clone and mutate it; otherwise, new random players are generated.
        """
        self.doodlers = [
            Player.Player(best_brain.clone() if best_brain else nn.NeuralNetwork(5, 4, 3))
            for _ in range(total)
        ]
        return self.doodlers

    def next_generation(self, total, players):
        """
        Create the next generation from the current population.
        """
        # Find the best player of the current generation
        self.best_one(players)

        # Add a clone of the best player (unmutated)
        champion = self.best.clone()
        champion.fitness = self.best_fitness
        self.doodlers.append(Player.Player(champion.brain))

        # Fill the remaining slots with mutated offspring
        fitness_sum = self.calculate_fitness_sum(players)
        for _ in range(total - 1):
            parent = self.select_one(players, fitness_sum)
            child_brain = parent.clone()
            child_brain.mutate(0.1)
            self.doodlers.append(Player.Player(child_brain))

        # Clear the old population
        players.clear()

    def calculate_fitness_sum(self, players):
        """
        Calculate the total fitness of the current population.
        """
        return sum(player.fitness for player in players)

    def select_one(self, players, fitness_sum):
        """
        Select a player based on fitness-proportional probability (roulette selection).
        """
        rand = random.uniform(0, fitness_sum)
        running_sum = 0

        for player in players:
            running_sum += player.fitness
            if running_sum > rand:
                return player.brain

    def best_one(self, players):
        """
        Find the best player in the current population.
        """
        current_best = max(players, key=lambda p: p.fitness)

        if current_best.fitness > self.best_fitness:
            self.best = current_best.clone()
            self.best.fitness = current_best.fitness
            self.best_fitness = current_best.fitness
