def arabic2roman():
    arabic = raw_input("Enter an Arabic numeral: ")

    while arabic.isdigit() == False:
        print("Please enter a valid Arabic numeral (1, 2, 3, etc)")
        arabic = raw_input("Enter an Arabic numeral: ")

    print("You entered " + arabic)
    return 3

def test_arabic2roman():
    assert arabic2roman() == 3

arabic2roman()
