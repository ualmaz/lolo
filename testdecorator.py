def decor(func):
    def func_wrapper(text):
        if type(text) == int and float:
            print("It can be only string")
        else:
            return "{0}".format(func(text))
    return func_wrapper

@decor
def get_text(text):

    return "{0} end of line".format(text)

print(get_text('Beginning of line:   ...'))
