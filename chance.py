from pandas import *

data = read_csv("location.csv")

#extract columns from the csv to lists
column1 = data["#"].tolist()
column2 = data["Создатель"].tolist()

#store probabilities from column1 in the list
probability_list = []

#if there is a range, assign numbers to a and b (a = s[0], b = [-1])
for number in column1:
    if '–' in number:
        a = number[0]
        b = number[-1]
        probability = int(b) - int(a)
        probability_list.append(probability)
    else:
        probability_list.append(number)


#convert probability list to int
probability_list_int = list(map(int, probability_list))

#list = string from the column with character * probability  
products = []
for str, num in zip(column2, probability_list_int):
    products.append(str * num)
print(products)


    


