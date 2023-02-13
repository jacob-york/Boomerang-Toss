"""
Practical Use Functions (puf)
"""


def clear():
    """Clears the console, regardless of OS."""
    from os import system, name
    
    system("cls" if name == "nt" else "clear")


'''
def get_varname(var):
    """Returns the variable's given name as a string."""
    return f'{var=}'.split("=")[0]
    # So this isn't going to work...
    # It just returns the formal parameter's name "var" and not the actual parameter.
'''


def get_menu(menu_name):
    """Returns a text document as a string
    (as long as the doc is in the same directory, of course)."""
    with open(menu_name + ".txt", "r") as menu:
        return menu.read()


'''
def num_get(prompt):
    """like input, but is purely for converting a user input to an int/float
    ex: prompt could be 'enter a number:' and num_get will convert it to an int/float automatically'"""
    string = input(prompt).replace(" ", "").replace(",", "")
    if string.isdigit():
        return int(string)
    elif string.replace(".", "").isdigit() and string.count(".") == 1:
        return float(string)
    elif string.replace(".", "").isdigit():
        return int(string.replace(".", ""))
    else:
        for char in string:
            if char not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
                string = string.replace(char, "")
        if string.isdigit():
            return int(string)
        elif string.replace(".", "").isdigit() and string.count(".") == 1:
            return float(string)
        elif string.count(".") > 2:
            string = string.replace(".", "")
            return int(string)


def Mike_Tyson(string):
    """
    replaces every s with th in a string (This is also a method for puc.NeoStr)
    for practical use, of course...
    """
    return string.replace("s", "th")


def random_date_beta(order="dmy", start=1920, end=2020) -> str:
    """
    -now outdated version that doesn't use class Date-
    generates a random date (String) in range start to end (defaults to 1920 to 2020).
    parameter "order" controls the order of random_date's return.
    (obviously, d=day, m=month, y=year)
    """
    import random
    random.seed()
    year = str(random.randint(start, end))
    month = str(random.randint(1, 12))
    if month == 2:
        if year % 4 == 0:
            lastDay = 29
        else:
            lastDay = 28
    elif month == 4 or 6 or 9 or 11:
        lastDay = 30
    else:
        lastDay = 31
    day = str(random.randint(1, lastDay))
    abbr = {"y": year, "m": month, "d": day}
    return abbr[order[0]] + "/" + abbr[order[1]] + "/" + abbr[order[2]]


def age_get_beta(dob, order="dmy") -> int:
    """
    -now outdated version of the Date method .age_get()-
    when passed a string (formatted like a date: 3/9/2001),
    age_get_beta will use localtime to find the age of a person, at the time of calling, who was born on dob.
    parameter "order" is used to tell age_get what order string dob is in.
    (obviously, d=day, m=month, y=year)
    """
    from time import localtime
    now = localtime()
    crntYear, crntMonth, crntDay = now[0], now[1], now[2]

    sect0 = int(dob[:dob.index("/")])  # -> X/x/x
    sect1 = int(dob[(dob.index("/") + 1):dob.index("/", (dob.index("/") + 1))])  # -> x/X/x
    sect2 = int(dob[(dob.index("/", (dob.index("/") + 1))+1):])  # -> x/x/X

    match = {order[0]: sect0, order[1]: sect1, order[2]: sect2}
    
    dayOB = match["d"]
    monthOB = match["m"]
    yearOB = match["y"]

    yearsPassed = (crntYear - 1) - yearOB
    if crntMonth < monthOB:
        return yearsPassed
    elif crntMonth > monthOB:
        return yearsPassed + 1
    elif crntMonth == monthOB:
        if crntDay >= dayOB:
            return yearsPassed + 1
        else:
            return yearsPassed
'''
