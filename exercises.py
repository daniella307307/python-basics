
#this structure will faclitate aggregation, sorting , filtering and reduce the compleity of the data
cars = [
       {'location': 'Gasabo', 'car_name': 'Ford', 'year': 2005, 'car_price': 5000, 'car_owner': 'Alice'},
       {'location': 'Gasabo', 'car_name': 'Mitsubishi', 'year': 2000, 'car_price': 3000, 'car_owner': 'Bob'},
       {'location': 'Gasabo', 'car_name': 'BMW', 'year': 2019, 'car_price': 25000, 'car_owner': 'Charlie'},
       {'location': 'Gasabo', 'car_name': 'VW', 'year': 2011, 'car_price': 12000, 'car_owner': 'David'},
       {'location': 'Kicukiro', 'car_name': 'Toyota', 'year': 2018, 'car_price': 22000, 'car_owner': 'Eve'},
       {'location': 'Kicukiro', 'car_name': 'Honda', 'year': 2015, 'car_price': 18000, 'car_owner': 'Frank'},
       {'location': 'Kicukiro', 'car_name': 'Subaru', 'year': 2020, 'car_price': 27000, 'car_owner': 'Grace'},
       {'location': 'Kicukiro', 'car_name': 'Nissan', 'year': 2017, 'car_price': 20000, 'car_owner': 'Heidi'},
       {'location': 'Nyarugenge', 'car_name': 'Chevrolet', 'year': 2016, 'car_price': 15000, 'car_owner': 'Ivan'},
       {'location': 'Nyarugenge', 'car_name': 'Hyundai', 'year': 2019, 'car_price': 21000, 'car_owner': 'Judy'},
       {'location': 'Nyarugenge', 'car_name': 'Kia', 'year': 2021, 'car_price': 23000, 'car_owner': 'Kevin'},
       {'location': 'Nyarugenge', 'car_name': 'Mazda', 'year': 2014, 'car_price': 16000, 'car_owner': 'Laura'}

]

#filter cars from Gasabo and sort by car price in ascending order
# sorted_cars = sorted(cars , key = lambda x:x['car_price'])
# print (sorted_cars)
def bubble_sort(cars):
    n = len(cars)
    for i in range(n):
        for j in range(0, n-i-1):
            if cars[j]['car_price'] > cars[j+1]['car_price']:
                cars[j], cars[j+1] = cars[j+1], cars[j]
    return cars
# def insertion_sort(cars):
#     for i in range(1, len(cars)):
#         key = cars[i]
#         j = i-1
#         while j >=0 and key['car_price'] < cars[j]['car_price']:
#             cars[j+1] = cars[j]
#             j -= 1
#         cars[j+1] = key
#     return car
sorted_cars = bubble_sort(cars)
# sorted_cars = insertion_sort(cars)  

#returnign the total price of all cars
total_price = sum(car['car_price'] for car in cars)
print (total_price)

#returning the total price for cars in Nyarugenge
total_price_Nyarugenge = sum(car['car_price'] for car in cars if car['location'] == 'Nyarugenge')
print(total_price_Nyarugenge)

#returning the cheapest car location
cheapest_car = min(cars, key=lambda car:car['car_price'])
print(cheapest_car['location'])

#returning a list of available car names
car_names = [car['car_name'] for car in cars]
print(car_names)

#addign a new brand name
brand_name = ['Audi', 'Tesla']
car_names.extend(brand_name)
car_names_sorted = sorted(car_names)
print(car_names_sorted)

#getting all classNames except the first one
print(car_names[1:])

#unpacking
car1, car2, *rest= car_names
print(car1, car2)

car1, car2, *remaining_cars = car_names
print(remaining_cars)

# replace the second to fourth car names with "tesla" and 'volvo'
car_names[1:4] = ['Tesla', 'Volvo']
print(car_names)

car_names[1]= ['Tesla', 'Volvo']

car_names[2]= ['Hybrid car']
print(car_names)

car_names[1:4]= ['Electric car']
print(car_names)

#getting the length of a list
number_of_cars = len(cars)
print(number_of_cars)