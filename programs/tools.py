import datetime
import random

def new_id():
    # Obtenez l'heure actuelle avec une précision jusqu'aux microsecondes
    current_time = datetime.datetime.now()
    # Générez un identifiant unique en combinant l'heure actuelle et un nombre aléatoire
    unique_id = current_time.strftime("%Y%m%d%H%M%S%f") + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    return unique_id

print(new_id())
