def verse(number):
    if number == 0:
        return("No more bottles of beer on the wall, "
            "no more bottles of beer.\nGo to the store and buy some more, "
            "99 bottles of beer on the wall.\n")

    elif number == 1:
        return("1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n")
    elif number == 2:
        return("2 bottles of beer on the wall, 2 bottles of beer.\n"
                "Take one down and pass it around, "
                "1 bottle of beer on the wall.\n")
    else:
        return("%s bottles of beer on the wall, %s bottles of beer.\n"
                "Take one down and pass it around, "
                "%s bottles of beer on the wall.\n" % (number, number, number - 1))



def song(number1, number2=0):
    verses = ""
    for i in range(number1, number2 - 1, -1):
        verses += verse(i) + "\n"
    return verses
