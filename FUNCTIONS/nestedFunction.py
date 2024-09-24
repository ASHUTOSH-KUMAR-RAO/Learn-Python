def outer_function():
    x = 1

    def inner_function():
        y = 2
        ans = x+y
        return ans

    return inner_function()


output = outer_function()

print(output)
