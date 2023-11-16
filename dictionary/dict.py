'''
# Dictionary 

# get key from dict

dict = {"brand":"tata", "model":"nexon", "year":2020}
print(len(dict))
for x in dict:
    print(x)    # it will print key

print("####### print key vaule") 


## values() function for print keyvalue


for y in dict:
    print([y])   # it will print key value 

for i in dict.values():
    print(i)

#### item() function in dictionary 

dict = {"brand":"tata", "model":"nexon", "year":2020}

for x,y in dict.items():
    print(x,y)

#### modify in dictionary

dict1 = dict
dict1["year"] = 2022
print(dict1)
dict1["model"] = "SUV"
print(dict1)

#### find key in dictionary

if "model" in dict:
    print("model key is present in dict")

else:
    print("key is not found")


#### fromkeys function in dictionary

x=('first_ket', 'second_key', 'third_key')
y=123

dict1 = dict.fromkeys(x,y)   # create new dictionary from keys and values 
print(dict1)

'''
#### setdefault function in dictionary
 # this function use for checking item exist or not incase item does not exit it will be added into dictionary.

dict12 = {"brand":"tata", "model":"nexon", "year":2020}
xy= dict12.setdefault("color","white")
print(xy)
print(dict12)