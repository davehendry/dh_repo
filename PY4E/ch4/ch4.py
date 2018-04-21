def computepay(h,r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        pay = (40 * r) + ((h - 40)*(r * 1.5))
        return pay

hrs = input('Enter Hours Worked This Week: ')
rate = input('Enter Your Hourly Rate: ')
h = float(hrs)
r = float(rate)
x = computepay(h,r)
print(x)
