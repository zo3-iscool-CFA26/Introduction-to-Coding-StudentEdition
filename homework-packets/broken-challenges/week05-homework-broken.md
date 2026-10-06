# Week 5 Broken Challenges

> **Glitch report:** The training loops are tangled. Some stop too soon, some
> repeat the wrong things, and Timo swears the vault is acting strange. Every
> problem has at least one bug. Watch for decoys, too.

Rules, tips, and the bug log are in [README.md](README.md). Runnable copies of
these programs are in [week05/](week05/).

## Problem 1 - Training-rep counter

File: [week05_p1_count_broken.py](week05/week05_p1_count_broken.py)

**Goal:** print the numbers from 1 to N.

```python
n = int(input("N: "))
for i in range(1, n):
    print(i)
```

### Test runs (when fixed)

```text
N: 5
1
2
3
4
5

N: 1
1
```

## Problem 2 - Even-energy crystals

File: [week05_p2_even_broken.py](week05/week05_p2_even_broken.py)

**Goal:** print the even numbers from 2 to N.

```python
n = int(input("N: "))
for i in range(1, n + 1, 2):
    print(I)
```

### Test runs (when fixed)

```text
N: 10
2
4
6
8
10

N: 7
2
4
6
```

## Problem 3 - Lina's spellbook drills

File: [week05_p3_table_broken.py](week05/week05_p3_table_broken.py)

**Goal:** ask for one number, then print its times table from 1 to 12.

```python
for i in range(0, 13):
    n = int(input("Number: "))
    print(n, "x", i, "=", n * i)
```

### Test runs (when fixed)

```text
Number: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
3 x 11 = 33
3 x 12 = 36
```

## Problem 4 - Vault retry loop

File: [week05_p4_retry_password_broken.py](week05/week05_p4_retry_password_broken.py)

**Goal:** keep asking until the correct password, `lion`, is entered.

```python
secret = "lion"
guess = input("Password: ")
While True:
    if guess == secret:
        print("Access granted")
        break
    print("Try again")
```

### Test runs (when fixed)

```text
Password: cat
Try again
Password: dog
Try again
Password: lion
Access granted

Password: lion
Access granted
```

## Problem 5 - Number-hunter puzzle

File: [week05_p5_guess_broken.py](week05/week05_p5_guess_broken.py)

**Goal:** the secret number is 11. After each wrong guess, give a "Too low" or
"Too high" hint, and keep asking until the player finds it.

```python
target = 11
while True:
    guess = input("Guess: ")
    if guess < target:
        print("Too high")
    elif guess > target:
        print("Too low")
    else:
        print("Correct")
    break
```

### Test runs (when fixed)

```text
Guess: 7
Too low
Guess: 11
Correct

Guess: 15
Too high
Guess: 3
Too low
Guess: 11
Correct
```
