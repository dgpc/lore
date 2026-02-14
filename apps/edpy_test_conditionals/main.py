import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

# Test: if statement
x = 5
if x > 3:
    Ed.PlayBeep()

# Test: if/else
y = 2
if y > 10:
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 10)
else:
    Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 10)

# Test: if/elif/else
z = 1
if z == 0:
    Ed.PlayBeep()
elif z == 1:
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 5)
else:
    Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 5)

# Test: comparison operators
a = 10
b = 20
if a < b:
    Ed.PlayBeep()
if a <= 10:
    Ed.PlayBeep()
if b >= 20:
    Ed.PlayBeep()
if a != b:
    Ed.PlayBeep()
