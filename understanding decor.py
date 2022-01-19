# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together#answer-739665
def shout(word="yes"):
    return word.capitalize()+"!"


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
        return word.lower()+"..."
    print(whisper())

talk()

try:
    print(whisper())
except NameError as e:
    print(e)


def gettalk(kind="shout"):
    def shout (word="yes"):
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

