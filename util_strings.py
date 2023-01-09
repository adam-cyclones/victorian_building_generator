# Easy String menipulation and formatting

def add_floor_suffix(number):
    if number % 100 in (11, 12, 13):
        return f"{number}th"
    elif number % 10 == 1:
        return f"{number}st"
    elif number % 10 == 2:
        return f"{number}nd"
    elif number % 10 == 3:
        return f"{number}rd"
    else:
        return f"{number}th"
