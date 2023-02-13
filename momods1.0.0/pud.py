"""
Practical Use Decorators (pud)
"""

def catch_unexpected(function):
    """Catches any unexpected errors. Useful during development and/or testing."""
    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            print("Unexpected Error:", type(e), e)
    return inner


def catch_error(function):
    """logs all Exceptions during function into a file called error_log.txt."""

    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            with open("error_log.txt", "a") as error_file:
                error_file.write(str(datetime.now()) + " " + str(type(e)) + ": " + str(e) + "\n")
            
    return inner


def ignore_if_error(function):
    """Skips the function if there is an error."""
    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except:
            pass
    return inner
    
        
def item_not_found(function):  # this is kinda dumb
    """
    handles errors related to things not existing or not being there.
    """
    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except (AttributeError,
            NameError,
            ImportError,
            IndexError,
            KeyError,
            ModuleNotFoundError,
            FileNotFoundError) as not_found:
            print(str(type(not_found)) + str(not_found))
    return inner


def must_be_string(function):
    """Used in setter methods to restrict the value to a string."""
    def inner(self, arg):
        if not isinstance(arg, str):
            raise TypeError("TypeError: \"" + str(arg) + "\" must be a string.")
        function(self, arg)
    return inner


def must_be_int(function):
    """Used in setter methods to restrict the value to an int."""
    def inner(self, arg):
        if not isinstance(arg, int):
            raise TypeError("TypeError: \"" + str(arg) + "\" must be an int.")
        function(self, arg)
    return inner
