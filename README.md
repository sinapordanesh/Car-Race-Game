
# Car Race Game


This is a simple game built using Pygame and Python where you control a jet that needs to pass through blocks coming from the top to bottom of the screen. The blocks increase in speed and randomize their positions as you progress through the game. This game is implemented using object-oriented programming (OOP) principles and utilizes an infinite loop as the game engine.
## Installation

To install and run Job Match locally, follow these steps:

1. Clone or download the repository
2. Install Pygame with the following command:

```cmd
pip install pygame
```

3. Run the game with the following command:

```cmd
python Main.py
```
## How to Play

- Press the spacebar to start the game
- Use the arrow keys (left, right) to control the jet
- The goal is to pass through the blocks without colliding with them
- As you progress through the game, the blocks will increase in speed and randomize their positions, making it more difficult

## OOP Design
The game is designed using OOP principles to keep the code modular and easy to maintain. The main game loop is an infinite loop that continuously updates the game state and renders the screen. The game loop is defined in the **CarRace** class, which also contains the logic for detecting collisions and updating the score.

The **CarRace** class represents the player-controlled jet, which is responsible for responding to user input and updating its position.


## Future Improvements

Some possible future improvements to this game could include adding sound effects, power-ups, or multiple levels with different block patterns. The game could also be made more visually appealing with improved graphics or animations. Additionally, adding a high-score system and a game over screen could enhance the player's experience.
## License

Job Match is licensed under the MIT license.