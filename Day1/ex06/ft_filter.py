def ft_filter(rule, iter):
    if rule: 
        return [x for x in iter if rule(x)]
    return [x for x in iter if x]

# def starts_a(w):
#     return w.startswith("a")

# def main():
#     li = ["line", "apple", "lemon", "army"]
#     res = ft_filter(starts_a, li)
#     print(res)

# if __name__ == "__main__":
#     main()