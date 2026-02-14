import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

# Test: simple function definition and call
def drive_square():
    for i in range(4):
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 10)
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 90)

drive_square()

# Test: function with parameters
def drive_polygon(sides, length):
    angle = 360 // sides
    for i in range(sides):
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, length)
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, angle)

drive_polygon(3, 15)

# Test: function with return value
def double(n):
    return n + n

dist = double(5)
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, dist)

# Test: recursion
def countdown(n):
    if n > 0:
        Ed.PlayBeep()
        Ed.TimeWait(300, Ed.TIME_MILLISECONDS)
        countdown(n - 1)

countdown(3)
