def debug(*args, **kwargs):
    print(f"DEBUG: {args}, {kwargs}")


number = int(input("Please enter a number: "))

if number > 0:
    # The "print" below is an example of some code
    # which is part of your program. This code could be
    # much more complicated and not necessarily generate output.
    print("A number is positve")
elif number < 0:
    debug("Here the number is negative!")
    debug("number", number)
    # The "print" below is an example of some code
    # which is part of your program. This code could be
    # much more complicated and not necessarily generate output.
    print("A number is negative")
else:
    # The "print" below is an example of some code
    # which is part of your program. This code could be
    # much more complicated and not necessarily generate output.
    print("A number is equal to 0")
