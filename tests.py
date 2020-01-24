from arabic2roman import arabic2roman


def test_normal():
    assert arabic2roman(34) == 'XXXIV'


def test_small():
    assert arabic2roman(2) == 'II'


def test_large():
    assert arabic2roman(3964) == 'MMMCMLXIV'


def test_out_of_range():
    assert arabic2roman(5678) == ''


def test_string():
    assert arabic2roman('hello') == ''


def test_mixed():
    assert arabic2roman('hel123lo') == ''


def test_float():
    assert arabic2roman(3.14) == ''


def test_start_num():
    assert arabic2roman('123hello') == ''
