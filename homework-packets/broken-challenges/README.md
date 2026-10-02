# Broken Challenges — The Glitch Raids the Archives

> **Story so far:** The Glitch's big attack is still weeks away, but a scouting
> swarm has already slipped into the Guild archives. It scrambled the answer
> scrolls for Weeks 1–5: the programs *look* like the answers you know, but every
> one of them is now broken. Grace, the Chief Bug-Hunter, is calling every
> apprentice to the hunt. Her motto: *"A clear error message is a gift."*

## How to play

1. Pick a week and open its challenge page (see [The challenges](#the-challenges)).
2. Read each program carefully and hunt for bugs.
3. Want to see what Python thinks? Run the matching file from that week's folder.
4. Record everything you find in your [bug log](#bug-log): the line, what is
   wrong, and the fix.
5. Fix the program and run it again. A problem is fixed when every test run on
   its challenge page matches **exactly**.

## Rules of the hunt

- **The bug count is secret.** Every problem has at least one bug, and some have
  more. Keep hunting until every test run matches.
- **Beware of decoys.** The Glitch also left a few lines that look strange but
  are perfectly valid Python. Flag only real bugs. Spotting a decoy, and
  explaining why it works, is a bug-hunting skill too.
- **One fix can reveal the next bug.** Python stops at the first error it meets,
  so run the program again after every fix.
- **Hunt with your own eyes.** Keep the `homework-answers/` folder closed until
  the debrief.

## The Glitch's bag of tricks

Every bug uses something you learned in Weeks 1–5:

- **Syntax:** mismatched quotes, missing or extra parentheses, missing colons
  `:`, missing commas, `=` where `==` belongs.
- **Indentation:** a line indented when it should not be, or not indented when
  it must be.
- **Names:** misspelled or wrongly capitalized variables and keywords.
- **Types:** text where a number belongs, or the wrong kind of number.
- **Logic:** the wrong operator, branches in the wrong order, or loops that run
  too many times, too few times, or never stop.
- **Output:** text that does not exactly match the expected output.

## Running a broken file

Open a terminal in this `broken-challenges` folder and run, for example:

```text
python week01/week01_p1_hello_broken.py
```

On some computers the command is `python3`. If a program gets stuck or floods
your screen, press **Ctrl+C** to stop it.

## The challenges

| Week | Challenge page                                         | Runnable files     |
| ---- | ------------------------------------------------------ | ------------------ |
| 1    | [week01-homework-broken.md](week01-homework-broken.md) | [week01/](week01/) |
| 2    | [week02-homework-broken.md](week02-homework-broken.md) | [week02/](week02/) |
| 3    | [week03-homework-broken.md](week03-homework-broken.md) | [week03/](week03/) |
| 4    | [week04-homework-broken.md](week04-homework-broken.md) | [week04/](week04/) |
| 5    | [week05-homework-broken.md](week05-homework-broken.md) | [week05/](week05/) |

## Bug log

Copy this table into your notes and add one row for each bug or decoy you find:

| Problem | Line | Bug or decoy? | What is going on? | Fix (bugs only) |
| ------- | ---- | ------------- | ----------------- | --------------- |
|         |      |               |                   |                 |
