import sys
import random


rhythm_games = sorted([
    "Beat Saber",
    "Cytus II",
    "Deemo",
    "VOEZ",
    "Muse Dash",
    "Tap Tap Reborn 2",
    "Dancing Line",
    "Lanota",
    "Arcaea",
    "SuperStar BTS",
    "Groove Coaster 2",
    "Tone Sphere",
    "Thumper: Pocket Edition",
    "Friday Night Funkin'",
    "Patapon: Rhythm Adventure",
    "Osu!stream",
    "Polyforge",
    "Lost in Harmony",
    "A Dance of Fire and Ice",
    "Dynamix",
    "Musiverse",
    "Pianista",
    "Beat Stomper",
    "Arkanoid vs Space Invaders",
    "Drag'n'Boom",
    "Thumper: Pocket Edition",
    "Aaero: A Melody of Movement",
    "Groove Planet",
    "Chameleon Run",
    "Electro Rush",
    "Polyblast",
    "Melobeat",
    "Zyon",
    "Beat Jumper",
    "Dancing Road: Color Ball Run!",
    "Groove Dance",
    "Hexologic",
    "Project Sekai"
])

def hold():
    class holder:
        def is_admin(self, _user_and_password: tuple[str, int|float|str]) -> bool | tuple[str, bool]:
            up = _user_and_password
            if len(up) > 1:
                if up[0] == 'Torrez':
                    if up[1] == 20111128:
                        return True
                    else:
                        return ("Error: {} was not the correct password for {}".format(up[2], up[1]), False)
                else:
                    if len(up) == 1:
                        return ("Error: {} wasn't recognised".format(up[1]), False)
                    elif len(up) == 2:
                        return ("Error: {} and {} wasn't recognised".format(up[1], up[2]), False)
                    else:
                        return ("Error: the arguments provided wasn't recognised", False)
    
    return holder()

class randrythm:
    class returnsion:
        def __new__(cls, _user_and_password: tuple[str, int|float|str]) -> bool | tuple[str, bool]:
            h = hold()
            if h.is_admin(_user_and_password):
                agemdryths = sorted([
                    "Project Sekai",
                    "Phigros"
                ])
                return random.choice(agemdryths)
            
            else:
                return random.choice(rhythm_games)
    
    class printration:
        def __init__(self):
            print(random.choice(rhythm_games))
