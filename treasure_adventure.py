def get_choice(prompt, options):
    """Ask until the player enters one of the available options."""
    valid_options = {option.lower() for option in options}

    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        print(f"Please choose one of: {', '.join(options)}.")


def play_game():
    health = 3
    has_potion = False

    print("\n" + "=" * 40)
    print("         THE LOST TEMPLE")
    print("=" * 40)
    print("Find the temple treasure and make it out safely!")
    print("You have 3 health points. Choose carefully.\n")

    path = get_choice(
        "You reach a fork in the trail. Take the forest or the river? ",
        ["forest", "river"],
    )

    if path == "forest":
        print("\nYou follow a quiet trail through the trees.")
        print("Beside an old camp, you find a bronze key and a healing potion.")
        has_potion = True
    else:
        print("\nYou wade through the river and spot a bronze key in the shallows.")
        print("The current knocks you against a rock. You lose 1 health.")
        health -= 1

    print(f"\nHealth: {health}/3")
    route = get_choice(
        "At the temple, do you use the locked gate or try the narrow tunnel? ",
        ["gate", "tunnel"],
    )

    if route == "gate":
        print("\nThe bronze key turns. The gate opens without a sound.")
    else:
        print("\nThe tunnel is full of sharp rocks. You scrape yourself and lose 1 health.")
        health -= 1

    if health <= 0:
        print("\nYou are too hurt to continue. The temple remains a mystery.")
        return

    print(f"\nHealth: {health}/3")
    if has_potion:
        use_potion = get_choice(
            "You still have a healing potion. Use it now? (yes/no) ",
            ["yes", "no"],
        )
        if use_potion == "yes":
            health = min(3, health + 1)
            print(f"The potion restores you. Health: {health}/3")

    print("\nA stone guardian blocks the treasure chest.")
    print('It asks: "The more you take, the more you leave behind. What am I?"')
    print("You have 3 guesses. A wrong answer costs 1 health.")

    for attempt in range(1, 4):
        answer = input(f"Guess {attempt}/3: ").strip().lower()
        if answer == "footsteps":
            print("\nThe guardian steps aside. You found the temple treasure. You win!")
            return

        print("That is not it.")
        health -= 1
        if health <= 0:
            print("The guardian sends you out of the temple. You ran out of health.")
            return
        print(f"Health: {health}/3")

    print('\nThe answer was "footsteps." The guardian closes the temple doors.')


def main():
    while True:
        play_game()
        again = get_choice("\nWould you like to play again? (yes/no) ", ["yes", "no"])
        if again == "no":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
