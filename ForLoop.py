# Get random names of the people in the list using For loop, maximum participant variable and input() function
# Get the lottery to run
max_participants = 10
participants = ["Luna", "Sol", "Venus", "Mars", "Gaia", "Hera", "Leto", "Persephone", "Nyx", "Astrid"]
import random
n = random.randint(0, max_participants-1)
participants[n]