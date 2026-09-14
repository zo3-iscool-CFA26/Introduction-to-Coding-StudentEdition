print("Temperature: 55")
temp = 55
rain = input("Raining? (yes/no): ").strip().lower()
if temp < 60 and rain == "yes":
    print("Advice: Wear a jacket a jacket and umbrella.")
elif temp < 60:
    print("Advice: Wear a jacket")
else:
  print("Advice: Light clothing is okay.")
