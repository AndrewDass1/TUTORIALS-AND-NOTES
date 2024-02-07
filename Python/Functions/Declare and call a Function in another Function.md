# Python: Declare and call a Function within a Function

```
# Define first function

def first_function():
    return "This is function 1"

# Define Second Function
def second_function():
    #Call function 1
    function1 = first_function()

    return function1

print(second_function())
```
