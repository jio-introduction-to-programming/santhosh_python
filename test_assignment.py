<<<<<<< HEAD
from assignment import (convert_to_int, find_max_of_numbers, get_char_from_num,
                        get_num_from_char, calculate_sum_of_numbers, check_type_of_value,
                        check_any_true_in_list, check_all_true_in_list, get_current_time)

def test_convert_to_int():
    assert convert_to_int('5') == 5
    assert convert_to_int('0') == 0
    assert convert_to_int('-3') == -3

def test_find_max_of_numbers():
    assert find_max_of_numbers([1, 2, 3, 4, 5]) == 5
    assert find_max_of_numbers([-1, -2, -3, -4, -5]) == -1
    assert find_max_of_numbers([0]) == 0

def test_get_char_from_num():
    assert get_char_from_num(65) == 'A'
    assert get_char_from_num(97) == 'a'
    assert get_char_from_num(48) == '0'

def test_get_num_from_char():
    assert get_num_from_char('A') == 65
    assert get_num_from_char('a') == 97
    assert get_num_from_char('0') == 48

def test_calculate_sum_of_numbers():
    assert calculate_sum_of_numbers([1, 2, 3, 4, 5]) == 15
    assert calculate_sum_of_numbers([-1, -2, -3, -4, -5]) == -15
    assert calculate_sum_of_numbers([0]) == 0

def test_check_type_of_value():
    assert check_type_of_value(5) == int
    assert check_type_of_value('hello') == str
    assert check_type_of_value([1, 2, 3]) == list

def test_check_any_true_in_list():
    assert check_any_true_in_list([0, False, None]) == False
    assert check_any_true_in_list([0, 1, False]) == True

def test_check_all_true_in_list():
    assert check_all_true_in_list([1, True, 'hello']) == True
    assert check_all_true_in_list([1, 0, 'hello']) == False

def test_get_current_time():
    import time
    assert abs(get_current_time() - time.time()) < 3600  # tested within 3600 seconds
=======
from assignment import ( add_one_to_number, add_two_numbers, subtract, 
                        sum_first_n_natural_numbers, divide_x_by_y_float, 
                        remainder_x_by_y, divide_x_by_y_numeric )

def test_add_one_to_number():
    assert add_one_to_number(1) == 2 
    assert add_one_to_number(5) == 6 

def test_add_two_numbers():
    assert add_two_numbers(5, 7) == 12 
    assert add_two_numbers(-4, -8) == -12 

def test_subtract():
    assert subtract(9, 11) == -2  
    assert subtract(-2, -2) == 0 
    assert subtract(100, 3) == 97 

def test_sum_first_n_natural_numbers():
    assert sum_first_n_natural_numbers(1) == 1 
    assert sum_first_n_natural_numbers(2) == 3 
    assert sum_first_n_natural_numbers(3) == 6 
    assert sum_first_n_natural_numbers(10) == 55 
    assert sum_first_n_natural_numbers(100) == 5050

def test_divide_x_by_y_float():
    assert divide_x_by_y_float(0, 12) == 0.0
    assert divide_x_by_y_float(90, 2) == 45.0
    assert divide_x_by_y_float(2, 10) == 0.2
    assert divide_x_by_y_float(-18, 36) == -0.5


def test_divide_x_by_y_numeric():
    assert divide_x_by_y_numeric(0, 12) == 0
    assert divide_x_by_y_numeric(90, 2) == 45
    assert divide_x_by_y_numeric(2, 10) == 0
    assert divide_x_by_y_numeric(-18, 36) == -1 

def test_remainder_x_by_y():
    assert remainder_x_by_y(10, 2) == 0
    assert remainder_x_by_y(0, 5) == 0
    assert remainder_x_by_y(27, 4) == 3 
    assert remainder_x_by_y(987, 10) == 7 
    assert remainder_x_by_y(93, 12) == 9 
>>>>>>> 6852cb01bcd9ce10e8dd645a11550b3ce8123581
