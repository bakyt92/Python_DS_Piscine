import time as time

x = time.time()
date_format = time.strftime("%B %d, %Y")
print("Seconds since January 1, 1970: ", "{:,.4f}".format(x), " seconds or in scientific notation: ", "{:e}".format(x)) 
print(date_format)

# https://docs.python.org/3/library/string.html#