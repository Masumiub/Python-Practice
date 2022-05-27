sh = input("Enter Hours: ")
sr = input("Enter Rate: ")


if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * .5)
    xp = reg + otp
else:
    xp = fh * fr
print(xp)
