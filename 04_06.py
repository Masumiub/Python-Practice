def computepay(h,r):
    if h > 40 :
        reg = h * r
        otp = (h - 40.0) * (r * .5)
        xp = reg + otp
    else:
        xp = h * r
    return xp

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    h = -1
    r = -1

p = computepay(h,r)
print("Pay",p)
