import random

adjectives = [
    'Extreme',
    'Dangerous',
    'Violent',
    'Sick',
    'Championship',
    'Air',
    'Lethal',
    'Imminent',
    'Murderous',
    'All out',
    'Flaming-hot',
    'Insane',
    'Mortal',
    'Lightning-fueled',
    'Superior',
    'Territorial',
    'Flaring',
    'Deserted',
    'Forceful',
    'Explosive'
]

words = [
    'Dogfight',
    'Kapow!',
    'Battle Royale',
    'Plane',
    'Battle',
    'Fight',
    'Bombardment',
    'Challenge',
    'Murder',
    'Warfare',
    'Interchange of gun bullets',
    'Combat',
    'Conquest',
    'Engagement',
    'Strikeforce',
    'Explosion',
    'Force'
]


def get_subtitle():
    a_sample_size = random.randint(1, 6)
    w_sample_size = random.randint(1, 7)
    l = random.sample(adjectives, a_sample_size) + random.sample(words, w_sample_size)
    l_with_newlines = []
    for i, word in enumerate(l):
        if i != 0 and i % 2 == 0:
            l_with_newlines.append(word + '\n')
        else:
            l_with_newlines.append(word)
    return ' '.join(l_with_newlines)

def get_number():
    # TODO use moon phase to determine number
    return random.randint(1, 20)

def get_name():
    return f"Toddstrike {get_number()}:\n{get_subtitle()}"
