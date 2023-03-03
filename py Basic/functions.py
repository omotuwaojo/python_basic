
def fun_name(pa1, pa2, pa3):
    x = pa1 *23
    pa3 = pa3*99
    value =pa1+pa2+pa3
    return value
x = fun_name(2, 33, 34)
print(x)

def is_even(num):
    if(num %2) == 0:
        return True
    else:
        return False
    print("anything")
print(is_even(2))

# optional
def count_down(x):
    if x == 1:
        print(x)
        return 1
    print(x)
    return count_down(x-1)
count_down(9)

#lambda expression-anonymos
#
def calculate_len(s):
    i =0;
    while(i < len(s)):
        i = i + 1
    return i 
print(calculate_len("12345678"))