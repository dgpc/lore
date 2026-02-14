import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

# This file documents Python features that EdPy does NOT support.
# The REMOTE compiler rejects these with errors (e.g., "constant 3.14 must be an integer value").
# The LOCAL mpy-cross compiler accepts them (it's a standard MicroPython compiler),
# but the resulting .mpy would fail or behave incorrectly on Edison firmware.

# Unsupported: string literals
message = "hello"

# Unsupported: float literals
pi = 3.14

# Unsupported: list literals
items = [1, 2, 3]

# Unsupported: dictionary literals
data = {1: 2}

# Unsupported: imports (other than Ed)
import math
