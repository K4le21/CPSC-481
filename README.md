# CPSC-481: AI Doodle Jump
An implementation of Doodle Jump using genetic algorithms and neural networks to train an AI "doodler" to play the game. Built upon an existing open-source Doodle Jump implementation, with added features for AI learning.

## Overview

The AI "doodler" uses a neural network with:
- 5 inputs (vision sensors and platform positions)
- 3 outputs (move left, right, or stay)
- 2 Hidden layers.
- Genetic algorithm for training across generations

## Features

- Two Game Modes:
  - Highscore Mode: "dooodler" tries to maximize its score without time limit
  - Time Trial Mode: "doodler" aims to maximize its score within 30 secs.
- Platform Types:
  - Green: Standard platforms
  - Blue: Moving platforms
  - Red: Breakable platforms
  - Springs: Power-ups for extra jump height
- Difficulty scaling based on score
- Automatic screen scrolling
- Generation tracking and performance logging

## Requirements

- Python 3.12.3 
- Pygame
- NumPy

## Installation

1. Clone the repository
```bash
git clone git@github.com:K4le21/CPSC-481.git
cd ai-doodle-jump
```

2. Install dependencies (if needed)
```bash
pip install pygame numpy
```

## Usage

Run the game:
```bash
python DoodleJump.py
```

Select game mode when prompted:
1. Highscore Mode
2. Time Trial Mode

## Files

- `DoodleJump.py`: Main game loop and display
- `Platform.py`: Platform generation and management
- `Player.py`: Player mechanics and AI "doodler" input processing
- `ga.py`: Genetic algorithm implementation
- `neuralnet.py`: Neural network architecture

## Results

The AI's performance is logged to 'v3_results.csv', tracking:
- Generation number
- Time alive
- Score achieved


## Contributors

- Kyle Chan @K4le21
- Ryan Lu @rlu132
- Tarmu Hu
- Enrique Gonzalez @egonzvlez

## Acknowledgments

Based on an open-source AI Doodle Jump implementation.
- https://github.com/EthanBautista/Doodle-Jump-AI
