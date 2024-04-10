import sys
x, y=input("enter x and y value: ").split()
x=int(x)
y=int(y)

def compare_result(var1,var2):
    if(var1*var2==8):
        var1=1
        print(var1)        
    else:
        var1=2
        print(var1)
       
    if(var1<var2):
        var1*=var1
        print(var1)        
    else:
        var1+=1
        print(var1)
        
    if(var1>var2):
        var1+=1
        var2+=1
        print(var1,var2)        
    else:
        var1-=1
        var2-=1
        print(var1,var2)
            

print(compare_result(x,y))
