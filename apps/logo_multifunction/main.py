import Ed

# Standard EdPy setup
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

def side():
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 10)

def square():
    for i0 in range(4):
        side()
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)

for i1 in range(3):
    square()
    Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 120)