import random

continents = {
    'Afro': ["algeria","egypt","cameroon","ghana","senegal","morocco","nigeria","south africa","tunisia"],
    'Euro': ["austria","belgium","bulgaria","croatia","czech rep","denmark","england","finland","france","germany","greece","iceland","ireland","italy","hungary","netherlands","norwege","poland","portugal","romania","russia","scotland","serbia","slovakia","slovenia","spain","sweeden","switherland","turkey","ukrania","wales"],
    'Asia': ["australia","china","iran","irak","japan","new zeeland","north korea","ksa","south korea","qatar"],
    'NA': ["costa rica","canada","mexico","jamaica","usa"],
    'SA': ["argentina","brazil","chile","colombia","ecuadro","panama","peru","uruguay"]
}

pots = []
T = random.sample(continents['Euro'], 13) + random.sample(continents['SA'], 4) + random.sample(continents['NA'], 4) + [random.choice(continents['NA'] + continents['SA'])] + random.sample(continents['Asia'], 5) + random.sample(continents['Afro'], 5)

for _ in range(4):
    random.shuffle(T)
    pots.append(T[:8])
    T = T[8:]

groups = {f'Group{i}': [] for i in range(1, 9)}

for group_num in range(1, 9):
    while len(groups[f'Group{group_num}']) < 4:
        pot_num = random.randint(0, 3)
        if not pots[pot_num]:
            continue
        country = random.choice(pots[pot_num])

        if country in groups[f'Group{group_num}']:
            continue

        if (pot_num == 0 and sum(1 for c in groups[f'Group{group_num}'] if c in continents['Euro']) >= 2) or \
                (pot_num == 1 and sum(1 for c in groups[f'Group{group_num}'] if c in continents['SA']) >= 1) or \
                (pot_num == 2 and sum(1 for c in groups[f'Group{group_num}'] if c in continents['NA']) >= 1) or \
                (pot_num == 3 and (sum(1 for c in groups[f'Group{group_num}'] if c in continents['NA']) >= 1 or
                                   sum(1 for c in groups[f'Group{group_num}'] if c in continents['SA']) >= 1)) or \
                (pot_num == 4 and sum(1 for c in groups[f'Group{group_num}'] if c in continents['Asia']) >= 1):
            continue

        groups[f'Group{group_num}'].append(country)
        pots[pot_num].remove(country)

# Print the final groups
for group_num, countries in groups.items():
    print(f'Group {group_num}: {", ".join(countries)}')

