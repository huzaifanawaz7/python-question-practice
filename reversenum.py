# def reverse_num(n):
#     re_num=""
#     for i in range (n):
#         if i<0:
#             break
#         else:
#             re_num+=str(i)
#     print("reverse numberof",n, " is ",re_num)
# reverse_num(12345)

def reverse_num(n):
    original = n
    reversed_num = 0
    
    while n > 0:
        last_digit = n % 10          # Gets the last digit (e.g., 5)
        reversed_num = (reversed_num * 10) + last_digit
        n = n // 10                  # Chops off the last digit
        
    print("reverse number of", original, "is", reversed_num)

reverse_num(12345)