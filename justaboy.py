import time

lyrics = [
    ("\nJust A Boy,Just A Boy..", 0.075),

    ("Makai No Sora De Pikapika\n", 0.075),

    ("Chiri Akuma Demo Kokoro Wa Pura", 0.075),

    ("Waratte Hashitte Dokki Dokki Ron\n", 0.075),  # thoda fast

    ("Chotto Hen Na Pawaa Ga Ban", 0.075),

    ("Kuroi Tsubasa Fura Fura Suwei\n", 0.050),

    ("Demo Yume Wa Akiramenu Brightness Play", 0.050),  # dramatic slow

    ("Kodomo Mitai Ni Hora Hora Oi\n", 0.060),  # fast vibe

    ("Ore Wa Madamada Just A Boy Aahhh Aaaa...\n", 0.060),

    ("Karada Juuden\n", 0.160),  # slow punch

    ("Tokimeku Hi\n", 0.160),

    ("Mawari Ga Ugoku..\n", 0.160)
]

for line, speed in lyrics:
    for char in line:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()