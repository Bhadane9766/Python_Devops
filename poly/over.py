class x:
    def m1(self):
        print("hello in X")
    
class y(x):
    def m1(self):
        print("hello in Y")
        super().m1()


y1=y()
y1.m1()

