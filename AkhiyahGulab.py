import time
import sys

# Golden / Yellow ANSI color
GOLD = "\033[93m"   # Bright Yellow
RESET = "\033[0m"

def print_lyrics():

    lyrics = [
        ("Kaisi Hai Lagdi Kamaal", 0.07, 1.0),
        ("Teri Ankhiyan Gulaab", 0.08, 1.0),
        ("Ke Na Jaave Sadda Pyar", 0.07, 0.8),
        ("Tainu Chhadd Ke", 0.09, 1.2),
        ("Ho Jaave Tera Hi Deedar", 0.07, 0.8),
        ("Te Koyi Na Sambhal Vi", 0.06, 0.7),
        ("Paave Sadda Pyar", 0.07, 0.9),
        ("Tu Chhadd Ke", 0.09, 1.3),
        ("Teri Raza Teri Zameen", 0.07, 0.8),
        ("Tere Iraade Ho Na", 0.07, 0.8),
        ("Teri Kami Hove Kabhi", 0.08, 1.0),
        ("Mere Kareeb Reh", 0.10, 2.0)
    ]

    print(GOLD + "\n--- Romantic Golden Mode ---\n" + RESET)
    time.sleep(1)

    for line, speed, pause in lyrics:
        for char in line:
            sys.stdout.write(GOLD + char + RESET)
            sys.stdout.flush()
            time.sleep(speed)
        print()
        time.sleep(pause)

print_lyrics()