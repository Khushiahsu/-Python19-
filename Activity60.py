#Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip?

def hotelcost(night):
    return 100*night

    
def planecost(city):
    if 'London'==city:
        return 150
    elif 'Paris'==city:
        return 175
    else:
        return 250
    
def vehiclecost(days):
    if days>=7:
        return 60*days-50
    elif days>=3:
        return 60*days-20
    else:
        return 60*days
    
def trip_cost(city,days,spendingmoney):
    return vehiclecost(days)+hotelcost(days)+planecost(city)+spendingmoney
print('Cost of car rental:', vehiclecost(6))
print('Cost of plane ticket is:', planecost('Italy'))
print('Cost of hotel cost is :', hotelcost(6))
print('Cost of trip is:', trip_cost('Italy',6,6000))