import Ed

# Standard EdPy setup
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

for i0 in range(3):
    for i1 in range(4):
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 5)
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 10)
    Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 120)