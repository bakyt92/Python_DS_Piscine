import matplotlib.image as mpimg

def ft_load(path: str) -> array: 
    try:
        img = mpimg.imread(path)
    except :
        print("Assertion error: ", {error})
