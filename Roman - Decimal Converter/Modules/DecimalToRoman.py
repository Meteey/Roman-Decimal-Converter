def number_describer(number, normal, big, bigger):
    normal_sign = ""
    big_sign = ""
    bigger_sign = ""
    translated_num = ""
    if normal == 1:
        normal_sign = "I"
        big_sign = "V"
        bigger_sign = "X"

    elif normal == 10:
        normal_sign = "X"
        big_sign = "L"
        bigger_sign = "C"

    elif normal == 100:
        normal_sign = "C"
        big_sign = "D"
        bigger_sign = "M"

    if number < (big - normal):
        translated_num += normal_sign * (number // normal)
    elif number == big - normal:
        translated_num += normal_sign + big_sign
    elif number == big:
        translated_num += big_sign
    elif number < bigger - normal:
        translated_num += big_sign + normal_sign * ((number-big)//normal)
    elif number == bigger - normal:
        translated_num += normal_sign + bigger_sign
    elif number == bigger:
        translated_num = bigger_sign

    return translated_num


def main():
    try:
        number = int(input("Enter the number that you want to convert from decimal to roman:"))
        while number > 1000:
            number = int(input("Please enter an integer that is lower than 1001 to convert decimal to roman:"))
        remainder = number
        trans_num = ""
        while remainder != 0:
            if remainder <= 10:
                bigger = 10
                normal = 1
                big = 5
                num_that_ll_convert_in_this_level = remainder // normal
                remainder -= num_that_ll_convert_in_this_level * normal
                trans_num += number_describer(num_that_ll_convert_in_this_level * normal, normal, big, bigger)

            elif remainder <= 100:
                bigger = 100
                normal = 10
                big = 50
                num_that_ll_convert_in_this_level = remainder // normal
                remainder -= num_that_ll_convert_in_this_level * normal
                trans_num += number_describer(num_that_ll_convert_in_this_level * normal, normal, big, bigger)

            elif remainder <= 1000:
                bigger = 1000
                normal = 100
                big = 500
                num_that_ll_convert_in_this_level = remainder // normal
                remainder -= num_that_ll_convert_in_this_level * normal
                trans_num += number_describer(num_that_ll_convert_in_this_level*normal, normal, big, bigger)

        print(f"{number} in Romen Numerals : {trans_num}")
    except ValueError:
        print("Enter an integer")
        main()


if __name__ == '__main__':
    main()
