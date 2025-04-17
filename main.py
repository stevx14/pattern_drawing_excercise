# 🖼️ Python Pattern Drawing Project
import colorama
from colorama import Fore, Back, Style

# Step 1: Display a menu to the user
while True:

    print(Fore.GREEN + "🌟 Welcome to the Python Pattern Drawing Program!")
    print(Fore.GREEN + "Choose a pattern type:")
    print(Fore.CYAN + "1. Right-angled Triangle")
    print(Fore.RED + "2. Square with Hollow Center")
    print(Fore.BLUE + "3. Diamond")
    print(Fore.MAGENTA + "4. Left-angled Triangle")
    print(Fore.YELLOW + "5. Hollow Square")
    print(Fore.LIGHTRED_EX + "6. Pyramid")
    print(Fore.LIGHTGREEN_EX + "7. Reverse Pyramid")
    print(Fore.LIGHTBLUE_EX + "8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input(Fore.GREEN + "Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input(Fore.GREEN + "Enter the number of rows: "))
    elif choice in [2, 5, 8]:  # Patterns that need size
        size = int(input(Fore.GREEN + "Enter the size of the square/rectangle: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        for a in range(rows + 1):
            for b in range(a):
                print(Fore.CYAN+'*', end='')
            print('')

    elif choice == 2:  # Square with Hollow Center
        for a in range(size):
            for b in range(size):
                if a == 0 or a == size - 1 or b == 0 or b == size - 1:
                    print(Fore.RED+'*', end='')
                else:
                    print(' ', end='')

            print()

    elif choice == 3:  # Diamond
        middle = rows // 2 + 1
        for a in range(1, middle + 1):
            for b in range(middle - a):
                print(' ', end='')
            for b in range(a):
                print(Fore.BLUE + '*', end='')
            for b in range(a - 1):
                print(Fore.BLUE + '*', end='')
            print()

        for a in range(middle - 1, 0, -1):
            for b in range(middle - a):
                print(' ', end='')
            for b in range(a):
                print('*', end='')
            for b in range(a - 1):
                print('*', end='')
            print()


    elif choice == 4:  # Left-angled Triangle
        for a in range(rows, 0, -1):
            for b in range(a):
                print(Fore.MAGENTA + '*', end='')
            print('')


    elif choice == 5:  # Hollow Square
        for a in range(size):
            for b in range(size):
                if a == 0 or a == size - 1 or b == 0 or b == size - 1:
                    print(Fore.YELLOW + '*  ', end='')
                else:
                    print('   ', end='')

            print()
        pass

    elif choice == 6:  # Pyramid
        for a in range(rows):
            for b in range(rows - a):
                print(' ', end='')
            for b in range(a):
                print(Fore.LIGHTRED_EX + '*', end='')
            for b in range(a):
                print(Fore.LIGHTRED_EX + '*', end='')
            print(Fore.LIGHTRED_EX + '*')
        pass

    elif choice == 7:  # Reverse Pyramid
        for a in range(rows, 0, -1):
            for b in range(rows - a):
                print(' ', end='')
            for b in range(a):
                print(Fore.LIGHTGREEN_EX + '*', end='')
            for b in range(a - 1):
                print(Fore.LIGHTGREEN_EX + '*', end='')
            print()


    elif choice == 8:  # Rectangle with Hollow Center

        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for a in range(width):
            for b in range(height):
                if a == 0 or a == width - 1 or b == 0 or b == height - 1:
                    print(Fore.LIGHTBLUE_EX + '*', end='')
                else:
                    print(' ', end='')
            print()

    else:
        print("❌ Invalid choice! Please restart the program.")

    # Step 5: Optional - Allow the user to restart or exit

    restart = input(Fore.GREEN+"Do you want to draw another pattern? (y/n):").lower()
    if restart != 'y':
        print('Thanks for using the Python Pattern Drawing program. Bye!')
        break