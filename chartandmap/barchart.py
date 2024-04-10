import matplotlib.pyplot as plt



# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']
 
data = [23, 17, 35, 29, 12, 41]
 
# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)
 
# show plot
plt.show()