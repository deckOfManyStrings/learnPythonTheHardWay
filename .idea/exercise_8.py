#Exercise 8 shows how to do a more complicated formatting of a string

formatter = "{] {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your"
                       "Own text here"
                       "Maybe a peom"
                       "Or a song about fear"
                       ))