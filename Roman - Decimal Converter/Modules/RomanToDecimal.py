def basic_num(i):
    if i == "I":
        return 1
    elif i == "V":
        return 5
    elif i == "X":
        return 10
    elif i == "L":
        return 50
    elif i == "C":
        return 100
    elif i == "D":
        return 500
    elif i == "M":
        return 1000


def converter(roman):
    i = 0
    total_num = 0
    while i < len(roman):
        v1 = basic_num(str(roman[i]))
        if i + 1 < len(roman):
            v2 = basic_num(roman[i+1])
            if v2 > v1:
                total_num += v2-v1
                i += 2
            else:
                total_num += v1
                i += 1
        else:
            total_num += v1
            i += 1

    print(total_num)


def main():
    try:
        letters = ["I", "V", "X", "L", "C", "D", "M"]
        tetras = []

        for letter in letters:
            tetras.append(4 * letter)
        don_t_allowed = ["IL", "IC", "ID", "IM", "VX", "VL", "VC", "VD", "VM", "XD", "XM", "VV", "DD", "LL", "VVV",
                         "DDD" "LLL"]
        roman = input("Enter the number with using capitals:")

        for letter in roman:
            if letter not in ["I", "V", "X", "L", "C", "D", "M"]:
                main()
            for item in tetras:
                if item in roman:
                    main()
            for item in don_t_allowed:
                if item in roman:
                    main()
        converter(roman)


    except ValueError:
        print("Use letters as capitals")
        main()


if __name__ == '__main__':
    main()
