import Ed

# Standard EdPy setup
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 10)
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 10)
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 90)
Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 5)