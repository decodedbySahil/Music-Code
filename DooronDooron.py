import time
import sys

def print_lyrics():

    lyrics = [

        ("Sochu ke milni te bolaanga ki..", 0.09, 1.0),
        ("Teri taan gallaan ch... shaayari\n", 0.09, 1.0),
        ("Vekhegi mainu te sochegi kya tu..", 0.10, 1.0),
        ("Mitti da banda main, tu taan pari\n", 0.10, 0.11),
        ("Ishqe di galiyaan ch, khoya e dil ve..", 0.10, 0.5),
        ("Aas lagaaye ik jaaye tu mil ve\n", 0.10, 0.5),
        ("Kol tere mainu\n", 0.11, 0.4),
        ("Aan de soni\n", 0.10, 0.8),
        ("Karaan main kitne jatan O soni\n", 0.09, 0.9),
        ("Dooron dooron main...\n", 0.09, 0.98

    ]

    print("\nDooron Dooron :\n")
    time.sleep(1.2)

    for line, speed, pause in lyrics:

        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)  

        print()
        time.sleep(pause)


print_lyrics()