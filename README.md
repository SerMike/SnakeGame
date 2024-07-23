# Python Snake Game

A classic Snake game implemented in Python using the turtle module. Navigate the snake, eat food to grow, and try to achieve the highest score without hitting the walls or yourself!

## Features

- Smooth snake movement
- Randomly spawning food
- Score tracking
- Game over detection (wall collision and self-collision)
- Win condition (score of 100)
- Simple and clean graphics

## Prerequisites

- Python 3.x
- turtle module (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code.
2. Ensure you have Python 3.x installed on your system.
3. No additional dependencies are required.

## Usage

Run the game by executing the `main.py` file:

```
python main.py
```

## Controls

- Up Arrow: Move the snake upwards
- Down Arrow: Move the snake downwards
- Left Arrow: Move the snake to the left
- Right Arrow: Move the snake to the right

## Game Rules

1. Control the snake to eat the purple food dots.
2. Each food eaten increases your score and the length of the snake.
3. Avoid hitting the walls or the snake's own body.
4. The game ends if you collide with the wall or the snake's body.
5. Reach a score of 100 to win the game!

## Project Structure

- `main.py`: The main game loop and setup
- `snake.py`: Contains the Snake class that controls the snake's behavior
- `food.py`: Manages the food spawning and positioning
- `scoreboard.py`: Handles scoring and displays game messages


## License

This project is open source and available under the [MIT License](LICENSE).
