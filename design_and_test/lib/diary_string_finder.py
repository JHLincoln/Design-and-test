
def diary_string_finder(note, word):
    if note == [] and word == "":
        raise Exception ("Both inputs missing")
    elif note == [] and word != "":
        raise Exception ("List input missing")
    elif note != [] and word == "":
        raise Exception ("String input missing")
    
    for item in note:
        print (item)
        if word in item:
            return item
    return f"{word} not found in notes"


# note - list
# word - string

# return - line
# line - string (including keyword)