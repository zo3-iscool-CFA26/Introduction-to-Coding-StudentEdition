# Week 3 Broken Challenges

> **Glitch report:** Grace warned you that sloppy math lets the Glitch in, and
> she was right. The score, sparring, gate, provisioning, and climate scrolls
> are all compromised. Every problem has at least one bug. Watch for decoys,
> too.

Rules, tips, and the bug log are in [README.md](README.md). Runnable copies of
these programs are in [week03/](week03/).

## Problem 1 - Quest score math

File: [week03_p1_math_broken.py](week03/week03_p1_math_broken.py)

**Goal:** ask for two numbers and print their sum and product.

```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)
print("Product:", a x b)
```

### Test runs (when fixed)

```text
First number: 4
Second number: 6
Sum: 10
Product: 24

First number: 3
Second number: 5
Sum: 8
Product: 15
```

## Problem 2 - Sparring-match comparison

File: [week03_p2_compare_broken.py](week03/week03_p2_compare_broken.py)

**Goal:** ask for two numbers and print whether the first is greater.

```python
a = input("First number: ")
b = input("Second number: ")
print("First > Second:" a > b)
```

### Test runs (when fixed)

```text
First number: 9
Second number: 5
First > Second: True

First number: 10
Second number: 9
First > Second: True

First number: 3
Second number: 12
First > Second: False
```

## Problem 3 - Gate permission logic

File: [week03_p3_logic_broken.py](week03/week03_p3_logic_broken.py)

**Goal:** the gate opens only for heroes who are 13 or older and have
permission.

```python
age = int(input("Age: "))
permission = input("Permission (yes/no): ").strip().lower()
print("Allowed:", age >= 13 or permission == "Yes")
```

### Test runs (when fixed)

```text
Age: 14
Permission (yes/no): yes
Allowed: True

Age: 14
Permission (yes/no): no
Allowed: False

Age: 10
Permission (yes/no): yes
Allowed: False

Age: 13
Permission (yes/no): YES
Allowed: True
```

## Problem 4 - Provisioning planner

File: [week03_p4_snacks_broken.py](week03/week03_p4_snacks_broken.py)

**Goal:** total snacks = players × snacks each.

```python
players = float(input("Players: "))
snacks = int(input("Snacks each: ")))
print("Total snacks:", players * snacks)
```

### Test runs (when fixed)

```text
Players: 6
Snacks each: 3
Total snacks: 18
```

## Problem 5 - Climate converter

File: [week03_p5_temp_broken.py](week03/week03_p5_temp_broken.py)

**Goal:** convert a Fahrenheit temperature to Celsius.

```python
f = float( input("Fahrenheit: ") )
c = f - 32 * 5 / 9
print("Celcius:", c)
```

### Test runs (when fixed)

```text
Fahrenheit: 68
Celsius: 20.0

Fahrenheit: 212
Celsius: 100.0

Fahrenheit: 32
Celsius: 0.0
```
