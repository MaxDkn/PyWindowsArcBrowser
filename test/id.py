import datetime
import random

def generate_unique_id():
    # Obtenez l'heure actuelle avec une précision jusqu'aux microsecondes
    current_time = datetime.datetime.now()
    
    # Générez un identifiant unique en combinant l'heure actuelle et un nombre aléatoire
    unique_id = current_time.strftime("%Y%m%d%H%M%S%f") + str(random.randint(0, 999999))
    
    return unique_id
