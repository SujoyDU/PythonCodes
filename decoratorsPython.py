def check_function_value(func):
    def helper(x):
        if x != 0 :
            return func(x)
        else :
           print('integer value can not be divided by 0')
    return helper


@check_function_value
def divide_by(x):
    print(f'100 divided by {x} is {100/x:.3f}')

divide_by(0)