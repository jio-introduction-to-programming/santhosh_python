<<<<<<< HEAD
def convert_to_int(x):
    '''
        Task-1 Convert x to int and return the result 
    '''
    result = int(x) # write your code here ! 
    return result 

def find_max_of_numbers(numbers):
    '''
        Task-2 Find and return the maximum number from the list numbers
    '''
    result = max(numbers) # write your code here ! 
    return result 

def get_char_from_num(num):
    '''
        Task-3 Get a character that corresponds to num in Unicode and return the result
    '''
    result = chr(num) # write your code here ! 
    return result 

def get_num_from_char(char):
    '''
        Task-4 Get a number that corresponds to char in Unicode and return the result
    '''
    result = ord(char) # write your code here ! 
    return result 

def calculate_sum_of_numbers(numbers):
    '''
        Task-5 Calculate and return the sum of numbers in the list numbers
    '''
    result = sum(numbers) # write your code here ! 
    return result 

def check_type_of_value(val):
    '''
        Task-6 Check and return the type of val
    '''
    result = type(val) # write your code here ! 
    return result 

def check_any_true_in_list(lst):
    '''
        Task-7 Check if any of the value in the list lst is True
    '''
    result = any(lst) # write your code here ! 
    return result 

def check_all_true_in_list(lst):
    '''
        Task-8 Check if all of the values in the list lst are True
    '''
    result = all(lst) # write your code here ! 
    return result 

def get_current_time():
    '''
        Task-9 Get and return the current time in seconds since the Epoch
    '''
    import time
    result = time.time() # write your code here ! 
    return result 
=======

def add_one_to_number(x):
    '''
        Task-1 Write the code below to add 1 to a number 
        and remove the pass statement 
    '''
    result = x + 1  # write your code here and replace None with the actual value 
    return result 

def add_two_numbers(x, y):
    '''
        Task-2 remove the pass statement and return the sum of 
        2 numbers  
    ''' 
    result = x+y # write your code here ! 
    return result 

def subtract(x, y):
    '''
        Task-3 subtract y from x and return the result 
    '''
    result = x-y # write your code here ! 
    return result 


def sum_first_n_natural_numbers(n):
    '''
        Natural numbers are 1 -> infinity 
    '''
    if n < 1:
        return n
    result = (n*(n+1))/2 # write your code here 
    return result 

def divide_x_by_y_float(x, y):
    '''
        Division by zero is not defined 
        Return the result of x divided by y as a float 
    '''
    if y == 0:
        return  y
    result = x/y # replace None with your code 
    return result 

def divide_x_by_y_numeric(x, y):
    '''
        Return the result of x divided by y as a numeric without decimals 
    '''
    if y == 0:
        return y
    result = x//y # replace None with your code 
    return result 

def remainder_x_by_y(x, y):
    '''
        Remainder when x is divided by y 
    ''' 
    result = x%y # replace None with your code 
    return result 
>>>>>>> 6852cb01bcd9ce10e8dd645a11550b3ce8123581
