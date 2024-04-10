import json
import matplotlib.pyplot as plt
    

def plot_graph(name,age):
    plt.plot(name,age)
    plt.show()
def sort_people():
    try:
        data = None
        name=[]
        age=[]
        color=[]
        with open("C:\\Users\\MU59BM\\source\\repos\\PythonTraining\\lists_data.json", "r") as infile:
            data=json.load(infile)
            print(data)
            for key in data:
                i=1
                if key=="Name":
                    name=data[key]
                if key=="Age":
                    age=data[key]
                if key=="color":
                    color=data[key]
                i+1
            print(name)
            print(age)
            print(color)
            plot_graph(name,age)
                         
    except:
        print("error")        
     

def get_people():
    try:
        name=['john','Rahul','Mark']
        age=[22,35,48]
        hair_color=['grey','black','white']
        
        
        data = {
                'Name': name,
                'Age': age,
                'color': hair_color
            }
        json_data = json.dumps(data, indent=4)
        with open("C:\\Users\\MU59BM\\source\\repos\\PythonTraining\\lists_data.json", "w") as outfile:
         outfile.write(json_data)
    except:
        print("check error")     


def main():
    get_people()
    sort_people()


if __name__ == '__main__':
    main()     
        
 

       
        


    
