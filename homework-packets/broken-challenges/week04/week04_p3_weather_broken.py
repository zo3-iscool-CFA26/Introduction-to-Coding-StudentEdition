temp = int(input("Temperature: "))
rain = input("Raining? (yes/no): ").lower().strip()
if temp < 60:
    print("Advice: Wear a jacket.")
elif temp < 60 and rain = "yes":
    print("Advice: Wear a jacket and bring an umbrella.")
else:
    print("Advice: Light clothing is okay.")
