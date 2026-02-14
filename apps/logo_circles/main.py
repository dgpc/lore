import Ed

# Standard EdPy setup
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

def circle():
    for i0 in range(360):
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 1)
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 1)

for i1 in range(45):
    circle()
    Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 8)