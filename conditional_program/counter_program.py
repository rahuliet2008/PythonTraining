

list=[]
number=int(input("enter numbers to be found greater than 7 between range 1 and 10 : "))
for i in range(number):
    value=int(input())
    list.append(value);


def compare_greater(usr_input):
    for i in usr_input:
        if(i>1 & i<10):
            print("value between 1 and 10 is : ", i)

print(compare_greater(list))            
      

        
