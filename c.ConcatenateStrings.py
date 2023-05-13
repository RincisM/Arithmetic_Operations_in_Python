a="Hello"
b="World"
c=" "
print("Four ways to Concatenate")
print("1.Using (+): ", a+c+b)
print("2.Using (join):",''.join([a,c,b]))
print("3.Using (format): {}{}{}".format(a,c, b))
print("4.Using (f-string): ", f'{a}{c}{b}')