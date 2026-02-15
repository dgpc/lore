# LOGO Language Reference

LORE includes a LOGO-to-EdPy transpiler that lets you program the Edison V3 robot using LOGO commands. Place a `main.logo` file in your app directory and LORE will automatically transpile it to EdPy Python before compilation.

## Movement

| Command | Description |
|---|---|
| `FORWARD expr` | Drive forward by `expr` units |
| `BACK expr` | Drive backward by `expr` units |
| `LEFT expr` | Spin left by `expr` degrees |
| `RIGHT expr` | Spin right by `expr` degrees |
| `STOP` | Stop driving |

```
FORWARD 50
RIGHT 90
FORWARD 50
STOP
```

## LEDs

| Command | Description |
|---|---|
| `LEDON` | Turn both LEDs on |
| `LEDOFF` | Turn both LEDs off |
| `LEFTLEDON` | Turn left LED on |
| `LEFTLEDOFF` | Turn left LED off |
| `RIGHTLEDON` | Turn right LED on |
| `RIGHTLEDOFF` | Turn right LED off |

```
LEDON
WAIT 2
LEDOFF
```

## Sound

| Command | Description |
|---|---|
| `BEEP` | Play a beep |
| `PLAYTONE note duration` | Play a tone at given frequency for given duration |

```
BEEP
PLAYTONE 440 2
```

## Timing

| Command | Description |
|---|---|
| `WAIT expr` | Wait for `expr` seconds |
| `WAITMS expr` | Wait for `expr` milliseconds |

```
FORWARD 10
WAIT 2
BACK 10
WAITMS 500
```

## Control Flow

| Command | Description |
|---|---|
| `REPEAT expr [ stmts ]` | Repeat statements `expr` times |
| `IF comparison [ stmts ]` | Execute statements if comparison is true |
| `IFELSE comparison [ stmts ] [ stmts ]` | If-then-else |
| `FOREVER [ stmts ]` | Loop forever |
| `WHILE comparison [ stmts ]` | Loop while comparison is true |

```
REPEAT 4 [FORWARD 50 RIGHT 90]

IF READKEYPAD > 0 [BEEP]

IFELSE READCLAP > 0 [LEDON] [LEDOFF]

FOREVER [
  IF READKEYPAD > 0 [STOP]
  WAIT 1
]

WHILE READDISTANCE < 50 [
  FORWARD 1
  WAITMS 100
]
```

## Variables

| Command | Description |
|---|---|
| `MAKE "name expr` | Set variable `name` to `expr` |
| `THING "name` | Read variable `name` (usable in expressions) |
| `:name` | Shorthand for reading a variable (in expressions) |

```
MAKE "distance 50
FORWARD :distance
FORWARD THING "distance
```

## User-Defined Functions

```
TO SQUARE :size
  REPEAT 4 [FORWARD :size RIGHT 90]
END

SQUARE 50
SQUARE 100
```

## Sensors

These return values and can be used in expressions and comparisons.

| Expression | Description | Returns |
|---|---|---|
| `READKEYPAD` | Read keypad state | 0=none, 1=triangle, 4=round |
| `READOBSTACLE` | Read obstacle detection | 0=none, 8=right, 16=ahead, 32=left |
| `READCLAP` | Read clap sensor | 0=not detected, 4=detected |
| `READLINE` | Read line tracker state | 0=white, 1=black |
| `READLEFTLIGHT` | Read left light level | 0-1023 |
| `READRIGHTLIGHT` | Read right light level | 0-1023 |
| `READDISTANCE` | Read left distance register | ticks remaining |

```
IF READOBSTACLE > 0 [STOP]
MAKE "light READLEFTLIGHT
```

## Sensor Setup

| Command | Description |
|---|---|
| `OBSTACLEBEAMON` | Enable obstacle detection IR beam |
| `OBSTACLEBEAMOFF` | Disable obstacle detection IR beam |
| `LINETRACKERON` | Enable line tracker LED |
| `LINETRACKEROFF` | Disable line tracker LED |
| `RESETDISTANCE` | Reset distance registers |

```
OBSTACLEBEAMON
RESETDISTANCE
WHILE READDISTANCE < 100 [
  IF READOBSTACLE > 0 [STOP]
  FORWARD 1
]
OBSTACLEBEAMOFF
```

## Arithmetic

Expressions support `+`, `-`, `*`, `/` (integer division) with standard precedence (`*` and `/` bind tighter than `+` and `-`).

```
MAKE "x 10 * 5
MAKE "y 100 / 4
FORWARD 3 * 2 + 1
FORWARD (3 + 2) * 10
```

## Comparisons

Supported comparison operators: `=`, `<`, `>`, `<=`, `>=`

```
IF :x >= 100 [BEEP]
WHILE READDISTANCE < 50 [FORWARD 1]
```
