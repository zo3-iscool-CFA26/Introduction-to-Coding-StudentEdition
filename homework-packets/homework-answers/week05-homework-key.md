# Week 5 Homework Teacher Key

## Problem 1 Solution

```python
n = int(input("N: "))
for i in range(1, n + 1):
    print(i)
```

### Problem 2 Solution

```python
n = int(input("N: "))
for i in range(2, n + 1, 2):
    print(i)
```

### Problem 3 Solution

```python
n = int(input("Number: "))
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")
```

### Problem 4 Solution

```python
secret = "lion"
while True:
    guess = input("Password: ")
    if guess == secret:
        print("Access granted")
        break
    print("Try again")
```

### Problem 5 Solution

```python
target = 11
while True:
    guess = int(input("Guess: "))
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("Correct")
        break
```
