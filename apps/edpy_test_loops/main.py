import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

# Test: for loop with range
for i in range(4):
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 10)
    Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)

# Test: while loop
count = 0
while count < 3:
    Ed.PlayBeep()
    Ed.TimeWait(500, Ed.TIME_MILLISECONDS)
    count = count + 1

# Test: nested for loops
for i in range(2):
    for j in range(3):
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 5)
