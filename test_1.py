import main


def test_calc_addition():
    output = main.calc_addition(2, 4)
    assert output == 6,"the output of 2 + 4 doesn't equal to 6."


def test_calc_subtraction():
    output = main.calc_subtraction(2, 4)
    assert output == -2,"the output of 2 - 4 doesn't equal to -2."


def test_calc_multiply():
    output = main.calc_multiply(2, 4)
    assert output == 8,"the output of 2 * 4 doesn't equal to 8."
