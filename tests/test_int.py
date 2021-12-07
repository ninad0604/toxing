from toxing import main

def test_int_greater_than_10():
    assert main.get_data() > 10

def test_type_int():
    assert type(main.get_data()) == int