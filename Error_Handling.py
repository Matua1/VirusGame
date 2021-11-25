#Error Handling an integer


def get_infected_percentage(num):
  num = int(num)
  if num >= 0:
    return (1 *(num))
  else:
    print("Invalid entry")
  
try:
    infected_percentage = input("Please enter the infected percentage number: ")
    print(get_infected_percentage(infected_percentage ))


except:
    print("Invalid entry, try again. ")


