#Question-1
def sum_list(lst):
    lst=[int(i) for i in lst]
    total_sum=sum(lst)
    return(total_sum)

#user_input = input("enter numbers:").split()
user_input=[1,2,3,4,5]
    
result = sum_list(user_input)
print("sum of elements given by you is: ",result)

#Question-2
def max_list(lst):
    lst=[int(i) for i in lst]
    max_element=max(lst)
    return(max_element)

#u_input = input("enter numbers:").split()
u_input=[1,3,4,5,67,5]
    
r = max_list(u_input)
print("maximum element is: ",r)

#Question-3
def reverse_list(lst):
    lst=[int(i) for i in lst]
    rev=lst[::-1]
    return(rev)

#usergiven_input = input("enter numbers:").split()
usergiven_input=[1,2,3,4,5,67,3]
    
res = reverse_list(usergiven_input)
print("reverse of the given list: ",res)

#Question-4
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                
                lst[j], lst[j+1] = lst[j+1], lst[j]  #swapping

        
#give_input = input("Enter a list of numbers:").split()
give_input=[1,2,4,5,67,7]
give_input = [int(num) for num in give_input]
bubble_sort(give_input)
print("Sorted list:", give_input)



#Question-5
def mean_list(lst):
    n1=len(lst)
    a= sum(lst)
    avg= a/n1
    return(avg)
lst=[1,2,3,4,5,6,7,8]
res1= mean_list(lst)
print("mean of the list is:",res1)

#mode calculation
def mode_list(lst):
    counts=0
    num=list[0]
    for x in lst:
        freq=lst.count(x)
        if (freq>counts):
            counts=freq
            num=x
    return num
lst=[1,1,1,1,1,11,2,2,2,3,3,3,4,4,4,4,4,55,5,5,5,5,5,67,7,7,8,8,8,6,55,5,5,3]
res2=mode_list(lst)
print(res2)

#Question-6

n = int(input("Enter the number of elements: "))
a=[]
for x in range(n):
    i=int(input("Enter the value of array: "))
    a.append(i)
    
k = int(input("Enter the key integer for a k sized-list: "))
b=[]
for j in range(k):
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))
    sum_start_to_end=int(sum(a[start:end+1]))
    b.append(sum_start_to_end)

print(b)

#Question-6

def sum_subarrays():
    # Step-1: Read a sequence of numbers as an input from user
    arr1 = list(map(int, input("Enter a sequence of numbers: ").split()))

    # Step-2: Read another integer k from the user
    k = int(input("Enter the number of subarrays to sum: "))

    # Initialize result list
    res4 = []

    # Step-3: Ask user to input two numbers start and end, k times
    for i in range(k):
        start, end = map(int, input(f"Enter start and end indices for subarray {i+1}: ").split())
        # Step-4: Return the sum of the array from start -> end as a result in the k-sized list
        result.append(sum(arr1[start:end+1]))

    return res4



    