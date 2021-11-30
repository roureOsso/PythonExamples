"""
Python's default arguments are evaluated once when the function is defined, not each time the function is called.
This means that if you use a mutable default argument and mutate it, you will and have mutated that object for all
future calls to the function as well.

SO:
Do not use mutable default arguments in Python, unless you have a REALLY good reason to do so.

Why? Because it can lead to all sorts of bugs, and the devil will haunt you.
"""


# Try it you self

def nasty_function(inputs=[]):
    inputs.append("something")
    return_values = ["items added"] + inputs
    return return_values


if __name__ == "__main__":
    print(nasty_function())

    # See how for the second call the item appended before remains in place
    print(nasty_function())

    # Of course if a different object is given this problem won't happen since the argument is evaluated again.
    print(nasty_function([""]))
