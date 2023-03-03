n1 = 5
n2 = 10
# greater than
n1_gt_n2 = n1 > n2 #returns a boolean
#print(n1_gt_n2)
# less than
n1_lt_n2 = n1 < n2
#print(n1_lt_n2)
password = input("password: ")
# 123456 = correct
correct_pass = "123456"
if password == correct_pass:
    print("correct password")
else:
    print("incorrect password")
if len(password) == 6:
    print("nice lenght")
else:
    print("too short password")