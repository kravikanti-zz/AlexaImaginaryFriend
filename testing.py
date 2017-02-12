# Kavya Ravikanti
# kr8nq

datafile = open("tvshows.csv","r")
tv_shows = []

for line in datafile:
    new_line = line.strip().split(",")
    tv_shows.append(new_line)

print(tv_shows)