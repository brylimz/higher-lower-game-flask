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

print("------acumulate decorators------")


def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\''''''/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")

    return wrapper


def sandwich(food="--ham--"):
    print(food)


sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()

print("--USING THE DECORATOR SYNTAX")


@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)


sandwich()

print("---ORDER DECORATORS MATTERS")


@ingredients
@bread
def strange_sandwich(food="--ham--"):
    print(food)


strange_sandwich()
# answering the question
print("------BOLD AND ITALIC ------")


def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"

    return wrapper


def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"

    return wrapper


@makebold
@makeitalic
def say():
    return "hello"


print(say())

# the next level of decorators
print("------ THE NEXT LEVEL OF DECORATORS ------")


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("I got args! Look: {0}, {1}".format(arg1, arg2))
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is {0} {1}".format(first_name, last_name))


print_full_name("Petter", "VS")

# decorating methods
print("----- decorating methods -----")


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_ur_age(self, lie):
        print(" I am {0}, what did you think?".format(self.age + lie))


I = Lucy()
I.say_ur_age(-3)
