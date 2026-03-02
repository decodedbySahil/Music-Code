import time
import sys

lyrics = [
    ("Pehla si tu pyaar..", 0.14, 0.3),

    ("Pehle pyaar di pehli kahaani\n", 0.06, 0.3),

    ("Badlaan vi kinjh hun?", 0.07, 0.3), 

    ("Chaah ke vi na badli jaani..\n", 0.06, 0.4),

    ("Mann vich main si raaja..", 0.05, 0.4),

    ("Tu kyun na meri bani ae raani?\n", 0.05, 0.5),  

    ("Khushiyan da main socheya..", 0.06, 0.5),

    ("Akkhan vich kyun de gayi paani?\n", 0.04, 0.8),

    ("Teriyan adavaan, teriyan adavaan", 0.08, 0.6),

    ("Munda maar sutteya tu, kaahda dil lutteya..\n", 0.08, 0.7),

    ("Tu mainu chhaddeya na kakh da", 0.09, 1.0),  

    ("Tu mainu chhaddeya na kakh da\n", 0.10, 1.2)
]

print("\nWith You: \n")
time.sleep(1)

for line, speed, pause in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)   # line-wise typing speed
    print()
    time.sleep(pause)      # line-wise pause