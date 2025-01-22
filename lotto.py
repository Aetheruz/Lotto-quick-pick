import random
from typing import List

def generate_numbers(min_num: int, max_num: int, num_picks: int) -> List[int]:
    """
    Generate a sorted list of random lottery numbers.
    
    Args:
        min_num: Minimum number in range
        max_num: Maximum number in range
        num_picks: Number of numbers to pick
    
    Returns:
        List of sorted random numbers
    """
    numbers = random.sample(range(min_num, max_num + 1), num_picks)
    return sorted(numbers)

def display_numbers(game_name: str, numbers: List[int]) -> None:
    """
    Display the lottery numbers in a formatted way.
    
    Args:
        game_name: Name of the lottery game
        numbers: List of numbers to display
    """
    print(f"\n{game_name} numbers: {' - '.join(map(str, numbers))}")

def main():
    # Game configurations
    GAMES = {
        "1": {"name": "Lotto 6/49", "picks": 6, "range": (1, 49)},
        "2": {"name": "Lotto Max", "picks": 7, "range": (1, 49)},
        "3": {"name": "Daily Grand", "picks": 5, "range": (1, 49)},
    }
    
    print("Welcome to the Lottery Number Generator!")
    
    while True:
        choice = input("\nWould you like to play the lottery? (yes/no): ").lower()
        
        if choice != "yes":
            break
            
        # Display game menu
        print("\nAvailable games:")
        for key, game in GAMES.items():
            print(f"{key}. {game['name']}")
        print("4. Exit")
        
        # Get game selection
        game_choice = input("\nSelect a game (1-4): ").strip()
        
        if game_choice == "4":
            break
            
        if game_choice not in GAMES:
            print("\nInvalid game selection. Please try again.")
            continue
            
        # Generate and display numbers for selected game
        game = GAMES[game_choice]
        numbers = generate_numbers(
            game["range"][0],
            game["range"][1],
            game["picks"]
        )
        display_numbers(game["name"], numbers)

    print("\nThanks for using the Lottery Number Generator!")

if __name__ == "__main__":
    main()