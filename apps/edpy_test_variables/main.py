import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

# Test: variable assignment and arithmetic
x = 10
y = 20
z = x + y

Ed.Drive(Ed.FORWARD, Ed.SPEED_5, z)

# Test: subtraction, multiplication, integer division, modulo
a = 100 - 30
b = 7 * 3
c = 20 // 3
d = 10 % 3

Ed.Drive(Ed.FORWARD, Ed.SPEED_5, a)

# Test: compound assignment
total = 0
total = total + 10
total = total + 20
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, total)

# Test: abs() builtin
neg = 0 - 15
pos = abs(neg)
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, pos)

# Test: reassignment
speed = 5
speed = 10
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, speed)
