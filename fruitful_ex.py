import sys

def turn_clockwise (orient):
    cardinals = ["n", "e", "s", "w", "n"]
    if orient in cardinals:
        return (cardinals[cardinals.index(orient)+1])


def day_name(number):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    try:
        return week[number]
    except IndexError:
        pass

def day_num(day):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    number = week.index(day)
    return number
    try:
        return week[day]
    except IndexError:
        pass

def test(did_pass):
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)



def test_suite():
    test(turn_clockwise("n") == "e")
    test(turn_clockwise("w") == "n")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
test_suite()
