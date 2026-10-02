# Week 4 Broken Challenges

> **Glitch report:** The Glitch has rigged BranchQuest's gates. Some lock the
> wrong heroes out, and some let the wrong heroes in. Every problem has at least
> one bug. Watch for decoys, too.

Rules, tips, and the bug log are in [README.md](README.md). Runnable copies of
these programs are in [week04/](week04/).

## Problem 1 - Apprentice trial checker

File: [week04_p1_pass_fail_broken.py](week04/week04_p1_pass_fail_broken.py)

**Goal:** a score of 70 or higher passes; anything lower fails.

```python
score = int(input("Score: "))
print("Result: Pass" if score > 70 else "Result: Fail")
```

### Test runs (when fixed)

```text
Score: 82
Result: Pass

Score: 70
Result: Pass

Score: 69
Result: Fail
```

## Problem 2 - Gatekeeper classifier

File: [week04_p2_ticket_broken.py](week04/week04_p2_ticket_broken.py)

**Goal:** child (under 13), teen (13 to 17), or adult (18 and up).

```python
age = int(input("Age: "))
if age < 13:
    print("Ticket type: Child")
if age < 18:
    print("Ticket type: Teen")
else
    print("Ticket type: Adult")
```

### Test runs (when fixed)

```text
Age: 15
Ticket type: Teen

Age: 10
Ticket type: Child

Age: 18
Ticket type: Adult
```

## Problem 3 - Traveler's advisor

File: [week04_p3_weather_broken.py](week04/week04_p3_weather_broken.py)

**Goal:** below 60 degrees and raining: jacket and umbrella. Below 60 and dry:
jacket. Otherwise: light clothing.

```python
temp = int(input("Temperature: "))
rain = input("Raining? (yes/no): ").lower().strip()
if temp < 60:
    print("Advice: Wear a jacket.")
elif temp < 60 and rain = "yes":
    print("Advice: Wear a jacket and bring an umbrella.")
else:
    print("Advice: Light clothing is okay.")
```

### Test runs (when fixed)

```text
Temperature: 55
Raining? (yes/no): yes
Advice: Wear a jacket and bring an umbrella.

Temperature: 55
Raining? (yes/no): no
Advice: Wear a jacket.

Temperature: 75
Raining? (yes/no): yes
Advice: Light clothing is okay.
```

## Problem 4 - Level gate

File: [week04_p4_level_gate_broken.py](week04/week04_p4_level_gate_broken.py)

**Goal:** level 10 and up: Open. Level 5 to 9: Almost. Below 5: Locked.

```python
level = int(input("Level: "))
if level >= 5:
    print("Gate status: Almost")
elif level >= 10:
    print("Gate status: Open")
else:
print("Gate status: Locked")
```

### Test runs (when fixed)

```text
Level: 4
Gate status: Locked

Level: 7
Gate status: Almost

Level: 12
Gate status: Open
```

## Problem 5 - Guild vault passcode

File: [week04_p5_password_check_broken.py](week04/week04_p5_password_check_broken.py)

**Goal:** compare the typed password to the stored password, `tiger123`.

```python
stored = tiger123
entered = int(input("Enter password: "))
print("Access granted" if entered != stored else "Access denied")
```

### Test runs (when fixed)

```text
Enter password: tiger123
Access granted

Enter password: lion
Access denied
```
