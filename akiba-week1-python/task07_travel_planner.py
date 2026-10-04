destination = input("Enter your Destination : ")
distance = float(input("Enter your Distance in kilometers : "))
average_speed = float(input("Enter your Average speed in km/h : "))

time = distance / average_speed

print(f" The approximate time taken to reach {destination} is : {time} hr")