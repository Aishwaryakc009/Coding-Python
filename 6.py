from time import sleep

def run():
    print("Press Ctrl+C to stop the second hand of the clock.")

    points_table = {}

    while True:
        name = input("\nEnter name of the player: ")
        points = 0
        attempts = 1

        while attempts <= 3:

            digit = 1

            while True:
                try:
                    print(digit)
                    sleep(0.2)

                    digit += 1
                    if digit == 13:
                        digit = 1

                except KeyboardInterrupt:
                    print(f"\nStopped at {digit}")

                    if digit in [1, 5, 9, 11]:
                        points += 10
                    elif digit in [4, 7, 8, 10]:
                        points += 20
                    else:
                        points += 30

                    print(f"Points: {points}")
                    attempts += 1
                    break

        points_table[name] = points
        print(f"{name} scored {points} points.")

        ans = input("Is there any other player (y/n)? ").strip().lower()

        if ans == "n":
            break

    print("\nFinal Results")
    for player, score in points_table.items():
        print(f"{player}: {score}")

    winner = max(points_table, key=points_table.get)
    print(f"\nWinner is {winner} with {points_table[winner]} points.")

run()