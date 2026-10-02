
from game_logic import play_game

def main():
    """Main execution loop to handle game replay."""
    while True:
        play_game()
        
        # Replay Option
        replay = input(" Do you want to play again? (y/n): ").lower().strip()
        if replay not in ("y", "yes"):
            print("\n Thanks for playing Snowman Meltdown! Goodbye!\n")
            break

    
if __name__ == "__main__":
    main()