# Week 2 Broken Challenges

> **Glitch report:** Lina's data scrolls are corrupted: the party greeter, the
> type detective, the time-scroll, the favorites wall, and the hero profile
> cards. Every problem has at least one bug. Watch for decoys, too.

Rules, tips, and the bug log are in [README.md](README.md). Runnable copies of
these programs are in [week02/](week02/).

## Problem 1 - Party greeter bot

File: [week02_p1_name_card_broken.py](week02/week02_p1_name_card_broken.py)

**Goal:** ask for a name and print a greeting.

```python
name = input("Enter your name: ")
print("Hello, {name}!")
```

### Test runs (when fixed)

```text
Enter your name: Alex
Hello, Alex!
```

## Problem 2 - Type detective with Lina

File: [week02_p2_types_broken.py](week02/week02_p2_types_broken.py)

**Goal:** make an `int`, a `float`, a string, and a `bool` variable, then print
each one's type.

```python
a = 3;
b = 2,5
c = "hello"
d = true
print(type(a), type(b), type(c), type(d), sep="\n")
```

### Expected output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Problem 3 - Time-scroll age checker

File: [week02_p3_age_next_year_broken.py](week02/week02_p3_age_next_year_broken.py)

**Goal:** ask for an age and print the age next year.

```python
age = input("Enter your age: ")
print("Next year you will be", age + "1")
```

### Test runs (when fixed)

```text
Enter your age: 13
Next year you will be 14

Enter your age: 9
Next year you will be 10
```

## Problem 4 - Party favorites wall

File: [week02_p4_favorites_broken.py](week02/week02_p4_favorites_broken.py)

**Goal:** ask for three favorites and print a summary.

```python
color = input("Favorite color: ")
game = input("Favorite game: ")
game = input("Favorite snack: ")
print(f"Summary: {color}, {snack}, {game}")
```

### Test runs (when fixed)

```text
Favorite color: blue
Favorite game: chess
Favorite snack: popcorn
Summary: blue, chess, popcorn
```

## Problem 5 - Hero profile card

File: [week02_p5_profile_card_broken.py](week02/week02_p5_profile_card_broken.py)

**Goal:** ask for a name, age, and hobby, then print a profile card.

```python
name = input("Name: ")
age = input("Age: ")
hobby = input("Hobby: ")
print(f"Name: {name}\nAge: (age)/nHobby: {hobby}")
```

### Test runs (when fixed)

The first three lines are the questions and your answers. The last three lines
are the printed card.

```text
Name: Alex
Age: 13
Hobby: Soccer
Name: Alex
Age: 13
Hobby: Soccer
```
