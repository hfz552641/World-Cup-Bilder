import random

# Define the list of countries grouped by continent
european_countries = ["Hungary", "Austria", "Czech Republic", "Wales", "Italy", "Greece", "Romania", "Turkey", "Croatia"]
african_countries = ["Cameroon", "Ghana", "Tunisia", "Morocco", "Senegal", "Algeria", "Nigeria", "South Africa"]
asian_countries = ["Japan", "Iran", "North Korea", "Iraq", "Saudi Arabia"]
american_countries = ["Argentina", "Canada", "Mexico", "Ecuador", "Jamaica", "Brazil", "Chile", "Uruguay", "Costa Rica", "Peru", "Panama", "Colombia", "USA"]

# Shuffle each list to select random teams
random.shuffle(european_countries)
random.shuffle(african_countries)
random.shuffle(asian_countries)
random.shuffle(american_countries)

# Create an empty list to hold the groups
groups = [[] for i in range(8)]

# Fill each group with a maximum of 2 European teams, 1 African team, 1 Asian team, and 1 American team
for i in range(8):
    # Add 1 African team
    groups[i].append(african_countries.pop())
    # Add 1 Asian team
    groups[i].append(asian_countries.pop())
    # Add 1 American team
    groups[i].append(american_countries.pop())
    # Add up to 2 European teams
    if len(european_countries) > 1:
        groups[i].extend(european_countries[:2])
        del european_countries[:2]
    elif len(european_countries) == 1:
        groups[i].append(european_countries.pop())

# Print the groups
for i in range(8):
    print(f"Group {i+1}: {', '.join(groups[i])}")
