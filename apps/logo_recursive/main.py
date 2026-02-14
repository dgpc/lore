import Ed

# Standard EdPy setup
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

def spiral(size):
    if size > 0:
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, size)
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)
        spiral((size - 1))

spiral(10)