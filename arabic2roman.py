# Laura Joy Erb
# EC500: Assignment 1
# Program to convert arabic numbers to roman numerals
# References:
    # https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/
    # https://www.101computing.net/number-only/

def arabic2roman():
    while True:
        try:
            arabic = int(input("Enter an Arabic numeral: "))
        except ValueError:
            print("Please enter a valid Arabic numeral (1, 2, 3, etc)")
            continue
        else:
            break

    # TODO: add checking for range of integers

    decimal = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    i = len(decimal)
    i -= 1

    while arabic > 0:
        rem = arabic // decimal[i]
        arabic = arabic % decimal[i]
        while rem > 0:
            rem -= 1
            print(romans[i], end = "")
        i -= 1
    print()
    return 3

def test_arabic2roman():
    assert arabic2roman() == 3

arabic2roman()
