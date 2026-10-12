# ================================ #
# PERSONAL GOALS DISPLAY           #
# ================================ #

# ---------- PART 1: import the keyword module ----------
import keyword  # One line. You need this for Part 7.

# ---------- PART 2: ask the three questions ----------
# Use input() three times and store each answer in its own variable.
# The text inside the quotes is the prompt the user sees.
person_name = input("Aaditya: ")
goal_name = input("editing: ")
target_month = input("november: ")

# ---------- PART 3: store the practice time ----------
daily_minutes = 30  # Store the number 30 in a variable called daily_minutes.
# Type it as 30, NOT as "30".

# ---------- PART 4: the heading ----------
# Print MY PERSONAL GOAL PLAN with one blank line above it and one below.
# Do it in a single print() using \n at the start and the end.
print("\nMY PERSONAL GOAL PLAN\n")

# ---------- PART 5: the four plan lines ----------
print("name:", person_name)
print("goal:", goal_name)
print("target month:", target_month)
print("daily practice:", daily_minutes, "minutes")

# ---------- PART 6: two lines that join up ----------
print("Status:", end=" ")
print("Not started")
print("Reminder:", end=" - ")
print("Practise every day!")

# ---------- PART 7: the sentence and the keywords ----------
print("\nIn one sentence:")
print(person_name, "will practice", goal_name, "for", daily_minutes, "minutes daily until", target_month + ".")
print("\nPython Keywords:")
print(keyword.kwlist)
