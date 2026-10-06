age = int(input("Age: "))
permission = input("Permission (yes/no): ").strip().lower()
print("Allowed:", age >= 13 or permission == "Yes")
