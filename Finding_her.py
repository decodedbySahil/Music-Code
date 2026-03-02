import time
import sys

lyrics = [
    "Sambhaal ke rakha wo phool mera tu\n",
    "Meri shayari mein zaroor raha tu\n",
    "Jo aankhon mein pyaari si duniya basaayi\n",
    "Wo duniya bhi tha tu, wo lamha bhi tha tu\n",
    "Haan, lagte hain mujhko ye kisse sataane\n",
    "Deta na dil mera tujhko bhulaane\n",
    "Adhoore se vaade, adhoori si raatein\n",
    "Ab hisse mein daakhil mere bas wo yaadein\n"
]


delays = [0.7, 0.7, 0.4, 0.5, 0.5, 0.7, 0.7, 1.0]

print("Finding Her:\n")
time.sleep(1.2)

for i, line in enumerate(lyrics):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)   

    print()  
    time.sleep(delays[i]) 