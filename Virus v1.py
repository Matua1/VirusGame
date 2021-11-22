#Purpose: Create a game that informs our school community about the virus

#A Virus simulator that encourages our Pap High community to learn more about Virus'
#Introduction to the Project
time.sleep(.05)
print("Welcome to the Pap High Virus Simulator\n Please follow the prompts: ")
#A requirement of this project will be to import a non-standard python library
import time


#Initiate user inputs
ctry_in = []
num_in = []
maxLengthList = 3

while len(ctry_in) < maxLengthList:
  
       ctry = str(input("Please enter the country name: ")).upper()
    if ctry != "":
      print("Invalid entry, please input a name. ")
       ctry_in.append(ctry)
       num_infected = int(input("Please enter the number infected: "))
    if num_infected != 0:
        print("Invalid entry, please try again. ")      
       num_in.append(num_infected)
     else:
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


for ctry in range(4):
    print(num_in, ctry_in)
    if num_in >= 5000:
        print("LOCKDOWN IS ESSENTIAL")

    else:
        print(num_in)

