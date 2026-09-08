age = 14
permission = "yes"
print("Age:" , age )
allowed = age >= 13 and permission == "yes"
print("Allowed:" , allowed)
permission = input("Permission (yes/no): ").strip().lower()
