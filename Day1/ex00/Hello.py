ft_list = ["Hello", "tata!"] 
ft_tuple = ("Hello", "toto!") 
ft_set = {"Hello", "tutu!"} 
ft_dict = {"Hello" : "titi!"} 

# list is mutable
ft_list[1] = "World"

# tuple is immutable -> we need it to convert to list, modify list and then convert it back to tuple
new_list = list(ft_tuple)
new_list[1] = "France"
ft_tuple = tuple(new_list)

# set is unordered and immutable but we can add and remove elements
ft_set.remove("tutu!")
ft_set.add("Paris")

# dictionary - mutable, key-value pairs
ft_dict["Hello"] = "42Paris"


print(ft_list) 
print(ft_tuple) 
print(ft_set) 
print(ft_dict)