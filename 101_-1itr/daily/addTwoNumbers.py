n1 = [2,4,9]
n2 = [5,6,4,9]

carry = 0

res = []
while n1 or n2:
    num1 = 0 if not n1 else n1.pop(0)
    num2 = 0 if not n2 else n2.pop(0)

    total = num1 + num2 + carry
    carry = total // 10
    digit = total % 10
    res.append(digit)



if carry:
    res.append(carry)
print(res)
    