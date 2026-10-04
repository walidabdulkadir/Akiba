destination = input("Enter your Destination : ")
distance = float(input("Enter your Distance in kilometers : "))
speed = float(input("Enter your Average speed in km/h : "))

time = distance / speed

print(f" The approximate time taken to reach {destination} is : {time} hr")