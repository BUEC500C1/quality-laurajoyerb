# Laura Joy Erb
# EC500: Assignment 1
# Program to convert arabic numbers to roman numerals
# References:
    # https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/
    # https://www.101computing.net/number-only/

def arabic2roman(arabic_num):
    try:
        arabic = int(arabic_num)
    except ValueError:
        print("Invalid arabic numeral. Please enter an integer value (1, 2, 3, etc)")
        return ''

    # TODO: add checking for range of integers

    decimal = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    i = len(decimal)
    i -= 1

    rom_numeral = ''

    while arabic > 0:
        rem = arabic // decimal[i]
        arabic = arabic % decimal[i]
        while rem > 0:
            rem -= 1
            rom_numeral += romans[i]
        i -= 1
    return rom_numeral
