def num1(x):
    def num2(y):
        return y
    return num2
print(num1("")(6))
