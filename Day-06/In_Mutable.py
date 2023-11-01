"""Mutable datatype: we can change the /edit/midify/delete the value in the same referance.

ex: list,dict, set"""


def demo(a):
    a = 10 
    a = a + 20
    print("the value of a is:", +a)


a = 100
print("main output", +a)

demo(a)




