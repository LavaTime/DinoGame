if obsList[x] == BIRD0 and obsPos[x][1] == bird_low_y:
    if (obsPos[x][0] - 96 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1] + 112 < bird_low_y):
        lose()
elif obsList[x] == BIRD0 and obsPos[x][1] == bird_mid_y:
    if obsPos[x][0] - 96 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1] + 112 < bird_mid_y:
        lose()
elif obsList[x] == BIRD0 and obsPos[x][1] == bird_high_y:
    if obsPos[x][0] - 96 < dinopos[0] < obsPos[x][0] + 92 and bird_high_y + 80 < dinopos[1] + 112 < bird_high_y:
        lose()
elif obsList[x] == CACTUSBIG:
    if (obsPos[x][0] - 60 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1] + 112 < cactusbig_y):
        lose()
elif obsList[x] == CACTUSHORD:
    if (obsPos[x][0] - 120 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1] + 112 < cactushord_y):
        lose()
elif obsList[x] == CACTUSSMALL:
    if (obsPos[x][0] - 40 < dinopos[0] < obsPos[x][0] + 92 and dinopos[1] + 112 < cactussmall_y):
        lose()