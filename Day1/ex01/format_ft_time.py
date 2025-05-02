import time 

x = time.time()

print("Seconds since January 1, 1970: ", "{:,.4f}".format(x), " seconds or in scientific notation: ", "{:e}".format(x)) 

# https://docs.python.org/3/library/string.html#