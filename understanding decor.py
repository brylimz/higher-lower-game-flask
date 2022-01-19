# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together#answer-739665
def shout(word="yes"):
    return word.capitalize() + "!"


print(shout())

scream = shout

del shout
try:
    print(shout())
except NameError as e:
    print(e)
print(scream())


def talk():
    def whisper(word="yes"):
        return word.lower() + "..."

    print(whisper())


talk()

try:
    print(whisper())
except NameError as e:
    print(e)


def gettalk(kind="shout"):
    def shout(word="yes"):
        return word.capitalize() + "!"

    def whisper(word="yes"):
        return word.lower() + "...."

    if kind == "shout":
        return shout
    else:
        return whisper


talk = gettalk()
print(talk)
print(talk())
print(gettalk("whisper")())


# handcrafted decorators


def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("before the function runs")

        a_function_to_decorate()

        print("after the function runs")

    return the_wrapper_around_the_original_function


def a_stand_alone_function():
    print("I am stand alone function, don't you dare modify me")


a_stand_alone_function()
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

print("with @ ---------")


@my_shiny_new_decorator
def another_stand_alone_function():
    print("leave me alone")


another_stand_alone_function()


# accumulate decorators

print("acumulate decorators")


def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\''''''/>")
    return wrapper()


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper()


def sandwich(food="--ham--"):
    print(food)