# Birthday Paradox
import datetime, random

def getBirthdays(numberofbirthdays):
    """ Returns a list of number random data objects for birthdays"""
    birthdays = []
    # year is not important
    for i in range(numberofbirthdays):
        startofyear = datetime.date(2001, 1, 1)

    # get random day into the year:
        randomnumberofdays = datetime.timedelta(random.randint(0, 364))
        birthday = startofyear + randomnumberofdays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # All Bdays are unique so return none

# compare each bday to every other bday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday

# display the intro:
print("Birthay Paradox")

# tuple of Months
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthdays shall I generate?(Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
    print()

# generate and display birthdays:
print("Here are", numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a coma for each birthday after the first birthday.
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display results
print('In this simulation,  ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print("multiple people have a birthday on", dateText)

else:
    print("No matching birthdays")

print()

# run through the 100000 simulations
print("Generating", numBDays, "random birthdays 100, 000 times...")
input("Press Enter to begin")

print('Let\'s run another 100, 000 simulations.')
simMatch = 0
for i in range(100_000):
    # Report on the progress every 10, 000 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100, 000 simulation run.")

# Simulation results
probabibility = round(simMatch / 100_000 * 100, 2)
print("Out of 100, 000 simulations of", numBDays, "people there was a")
print("matching birthday in that group", simMatch, "times. this means")
print("that", numBDays, "people have a", probabibility, "% chance of")
print("having a matching birthday in their group.")


