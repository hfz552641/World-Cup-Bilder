import random

# Define lists of countries for each region
Euro = ["Albania", "Austria", "Belgium", "Bosnia and Herzovico", "Bulgaria", "Croatia", "Czech Rep.", "Denmark", "England", "Finland", "France", "North Macedonia", "Germany", "Greece", "Hungary", "Iceland", "Ireland",
        "Italy", "Latvia", "Netherlands", "Northen Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweeden", "Switherland", "Turkey", "Ukraine", "Wales"]
Afro = ["Algeria", "Angola", "Benin", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Comoros", "Congo Rep.", "DRC", "Egypt", "Equatorial Guinea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bisseau",
        "Ivory Coast", "Kenya", "Madagashcar", "Malawi", "Mali", "Mauritania", "Morocco", "Namibia", "Niger", "Nigeria", "Senegal", "Sierra Leone", "South Africa", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
SA = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela"]
NA = ["Belize", "Bermuda", "Canada", "Costa Rica", "Cuba", "Curaco", "El Salvador", "French Guyana", "Grenada", "Guadelope", "Guatemela",
      "Guyana", "Haiti", "Honduras", "Jamaica", "Martinique", "Mexico", "Nicaragua", "Panama", "Suriname", "Trinidad and Tobago", "USA"]
Asia = ["Australia", "Bahrain", "China", "India", "Indonesia", "Iran", "Iraq", "Japan", "Jordan", "Kuwait", "Kygyzstan", "Lebanon", "Malaysia", "North Korea",
        "Oman", "Palestine", "Philippines", "Qatar", "KSA", "South Korea", "Syria", "Thailand", "Turkemenistan", "UAE", "Uzbakestan", "Vietnam", "Yemen"]
Oceania = ["New Zeeland","Tauvalu","Fiji","Solamon Islands"]

# Choose the host country randomly
Host = random.choice(Euro + Afro + SA + NA + Asia + Oceania)

# Function to select teams from a region while avoiding duplicates and the host
def select_teams(region_list, num_teams, host):
    teams = []
    while len(teams) < num_teams:
        team = random.choice(region_list)
        if team not in teams and team != host:
            teams.append(team)
    return teams

# Set the maximum number of teams for each region
max_teams = {
    "Afro": 2,
    "Asia": 3,
    "NA": 4,
    "SA": 5,
    "Oceania": 6
}

# Increase the maximum team count for a random region
choice = random.choice(list(max_teams.keys()))
max_teams[choice] += 1

# Select teams from each region based on the determined maximum number
QEuro = select_teams(Euro, 16, Host)
# Select teams from other regions similarly

# Create groups of teams for the tournament
groups = [QEuro[i:i+4] for i in range(0, len(QEuro), 4)]

# Output the groups
for i, group in enumerate(groups):
    print(f"Group {i + 1}: {group}")