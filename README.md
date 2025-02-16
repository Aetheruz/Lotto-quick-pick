# Lottery Number Generator

## Overview
The Lottery Number Generator is a simple Python script that randomly selects and displays lottery numbers for popular lottery games. Users can choose from predefined games and receive randomly generated numbers within the specified range.

## Features
- Supports three popular lottery games:
  - **Lotto 6/49**: Picks 6 numbers from 1 to 49
  - **Lotto Max**: Picks 7 numbers from 1 to 49
  - **Daily Grand**: Picks 5 numbers from 1 to 49
- Generates random, sorted lottery numbers.
- Allows users to play multiple rounds or exit at any time.

## Requirements
- Python 3.x

## Installation
No additional libraries are required. Ensure you have Python installed on your system.

## Usage
1. Run the script using:
   ```sh
   python lottery_generator.py
   ```
2. Follow the on-screen instructions:
   - Type **yes** to play or **no** to exit.
   - Select a lottery game from the available options.
   - The script will generate and display random lottery numbers.
   - You can play again or exit as desired.

## Code Structure
- `generate_numbers(min_num, max_num, num_picks)`: Generates random numbers within a given range.
- `display_numbers(game_name, numbers)`: Formats and displays the selected numbers.
- `main()`: Handles user interaction and game logic.

## Example Output
```
Welcome to the Lottery Number Generator!

Would you like to play the lottery? (yes/no): yes

Available games:
1. Lotto 6/49
2. Lotto Max
3. Daily Grand
4. Exit

Select a game (1-4): 1

Lotto 6/49 numbers: 4 - 12 - 23 - 34 - 42 - 48

Would you like to play the lottery? (yes/no): no

Thanks for using the Lottery Number Generator!
```

## License
This project is open-source and available for personal use and modifications.

## Author
James Romar Tuling
