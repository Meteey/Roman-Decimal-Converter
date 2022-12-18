import sys
from Modules import DecimalToRoman as dtr
from Modules import RomanToDecimal as rtd
sys.path.insert(0, 'Modules')


def take_options():
    try:
        option = int(input("1 or 2 (to exit enter 0):"))
        if option == 0:
            quit()
        elif option in [1, 2]:
            return option
        else:
            take_options()
    except ValueError:
        print("Enter 1, 2 or 0.")
        take_options()


def main():
    print("--------------------------", "\n"
                                        "  1-) Roman to decimal", "\n"
                                                                  "  2-) Decimal to roman")
    option = take_options()
    if option == 1:
        rtd.main()
    elif option == 2:
        dtr.main()

    continue_check = input("If you want to continue enter 1:")
    if continue_check == "1":
        main()


if __name__ == '__main__':
    main()
