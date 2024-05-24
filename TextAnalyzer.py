def txt_analyze(input):
    if type(input) != str:
        print(
            "Your input was not a string, I am changing it into a string, but note you might have an answer that doesn't make sense. /n    ----------")
        input = str(input)
    foo = list(input)
    if foo[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        reply1 = "Your string starts with an uppercase letter."
    elif foo[0] in "abcdefghijklmnopqrstuvwxyz":
        reply1 = "Your string starts with a lowercase letter."
    else:
        reply1 = "Your string doesn't seem to start with a letter I am familiar with."
    n = 0
    z = 0
    vcount = 0
    ccount = 0
    bar = len(input)
    reply3 = "Your string seems to have " + str(bar) + " characters in it (including spaces)."
    reply2Shape = []

    def counter(character):
        nonlocal ccount
        nonlocal vcount
        if character in "AEIOUaeiou":
            vcount += 1
        elif character in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            ccount += 1

    def characteruppercheck(character):
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            nonlocal z
            z += 1
            reply2Shape.append("Upper")
            return True
        else:
            return False

    def characterlowercheck(character):
        if character in "abcdefghijklmnopqrstuvwxyz":
            nonlocal z
            z += 1
            reply2Shape.append("Lower")
            return True
        else:
            return False

    def characterothercheck(character):
        if character not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ":
            nonlocal z
            z += 1
            reply2Shape.append("Other")
            return True
        else:
            return False

    while n < bar:
        counter(foo[n])
        n += 1

    n = 0
    while n < bar:
        if "Upper" not in reply2Shape:
            zoom = characteruppercheck(foo[n])
            if zoom == True:
                continue
        elif "Lower" not in reply2Shape:
            zoom = characterlowercheck(foo[n])
            if zoom == True:
                continue
        elif "Other" not in reply2Shape:
            zoom = characterothercheck(foo[n])

        if zoom == False:
            if "Lower" not in reply2Shape:
                zoom = characterlowercheck(foo[n])
            if zoom == False:
                if "Other" not in reply2Shape:
                    zoom = characterothercheck(foo[n])
        n += 1

    if z == 0:
        reply2 = "Your string doesn't seem to have any characters at all!"
    elif z == 1:
        if "Upper" in reply2Shape:
            reply2Temp = "uppercase characters"
        elif "Lower" in reply2Shape:
            reply2Temp = "lowercase characters"
        elif "Other" in reply2Shape:
            reply2Temp = "other characters"
        reply2 = "Your string has " + reply2Temp + " only."
    elif z == 3:
        reply2 = "Your string has a mix of all types of characters."
    elif z == 2:
        reply2Temp = []
        if "Upper" in reply2Shape:
            reply2Temp.append("uppercase characters")
        if "Lower" in reply2Shape:
            reply2Temp.append("lowercase characters")
        if "Other" in reply2Shape:
            reply2Temp.append("other characters")
        reply2 = "Your string has " + reply2Temp[0] + " and " + reply2Temp[1] + " in it."

    reply4 = "Your string has " + str(vcount) + " vowels and " + str(ccount) + " consonants in it."

    print(reply1)
    print(reply2)
    print(reply3)
    print(reply4)