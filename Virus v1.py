#Purpose: Create a game that informs our school community about the virus

#Initiate user inputs
ctry_in = []
num_in = []
maxLengthList = 3

while len(ctry_in) < maxLengthList:
  
    try:
       ctry = str(input("Please enter the country name: ")).upper()
       ctry_in.append(ctry)
       num_infected = int(input("Please enter the number infected: "))
       num_in.append(num_infected)
       ctry_num = "Your country is {} and Infected numbers are {}."
    except ValueError:
       print("please enter a number.")
    finally:
       ctry_num = "Your country is {} and Infected numbers are {}"
       print(ctry_num.format(ctry_in, num_in))


def update():   
  for i in range(3):
       ctry = str(input("Please enter the country name: ")).upper() 
       ctry_in.append(ctry)
       num_infected = int(input("Please enter the number infected: "))
       num_in.append(num_infected)
       ctry_num = "Your countries are: {} and Infected population numbers are {}"        
       print(ctry_num.format(ctry_in, num_in))
       
# this creates 5 iterations to gather data over a 5 day period.
def week_data():
    day = 0
     

print("Day 2:")
week_data()
update()
print("Day 3:")
week_data()
update()
print("Day 4:")
week_data()
update()
print("Day 5:")
week_data()
update()

for ctry in range(4):
    print(num_in, ctry_in)
    if num_in >= 5000:
        print("LOCKDOWN IS ESSENTIAL")

    else:
        print(num_in)

