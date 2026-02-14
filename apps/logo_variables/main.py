import Ed

# Standard EdPy setup
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

distance = 50
turn = 90
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, distance)
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, turn)
score = 75
if score >= 60:
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 100)
else:
    Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 20)
count = 0
for i0 in range(4):
    count = (count + 1)
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, distance)
    Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, turn)