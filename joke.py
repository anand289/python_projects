import pyjokes

def random_joke():
    joke = pyjokes.get_joke()
    print(joke)