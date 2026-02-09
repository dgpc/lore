import Ed

# Edison V3 setup
Ed.EdisonVersion = Ed.V3
Ed.Tempo = Ed.TEMPO_MEDIUM # Adjust tempo as needed
Ed.DistanceUnits = Ed.CM

# Define notes (simplified for common scales, EdPy might have specific mappings)
# EdPy's TuneString uses a specific notation for notes and durations.
# 'l' = low C, 'c' = C, 'd' = D, 'e' = E, 'f' = F, 'g' = G, 'a' = A, 'b' = B
# 'h' = high C etc.
# Durations are 1=whole, 2=half, 4=quarter, 8=eighth, 16=sixteenth

# Mary Had a Little Lamb
mary_tune_str = Ed.TuneString(52, "e4d4c4d4e4e4e4d4d4e4g4g4e4d4c4d4e4e4e4e4d4d4e4d4c4z")

# Twinkle Twinkle Little Star
twinkle_tune_str = Ed.TuneString(32, "c4c4g4g4a4a4g2f4f4e4e4d4d4c2z")

# Row, Row, Row Your Boat
row_tune_str = Ed.TuneString(37, "c4c4c8d8e4e4e8d8e8f8g4a4g4f4e4d4c2z")

# Define the number of tunes (for modulo arithmetic)
num_tunes = 3 

# Variables to store the current tune index
current_tune_index = 0

# Initial indication - e.g., 1 beep for tune 0, 2 beeps for tune 1, etc.
Ed.PlayBeep() # Indicate program start
Ed.TimeWait(500, Ed.TIME_MILLISECONDS)
# No Ed.EdisonPrint for initial message

# Function to play the currently selected tune
def play_current_tune(index):
    if index == 0:
        Ed.PlayTune(mary_tune_str)
    elif index == 1:
        Ed.PlayTune(twinkle_tune_str)
    elif index == 2:
        Ed.PlayTune(row_tune_str)

# Play first tune
play_current_tune(current_tune_index)

while True:
    # Check if music has ended to allow changing tune or replaying
    if Ed.ReadMusicEnd() == True:
        # Check for button presses
        key_pressed = Ed.ReadKeypad()

        if key_pressed == Ed.KEYPAD_ROUND:
            # Cycle to the next tune
            current_tune_index = (current_tune_index + 1) % num_tunes
            # Indicate new tune with beeps (e.g., 1 beep for tune 0, 2 for tune 1)
            if current_tune_index == 0:
                Ed.PlayBeep()
            elif current_tune_index == 1:
                Ed.PlayBeep()
                Ed.TimeWait(200, Ed.TIME_MILLISECONDS)
                Ed.PlayBeep()
            elif current_tune_index == 2:
                Ed.PlayBeep()
                Ed.TimeWait(200, Ed.TIME_MILLISECONDS)
                Ed.PlayBeep()
                Ed.TimeWait(200, Ed.TIME_MILLISECONDS)
                Ed.PlayBeep()
            
            play_current_tune(current_tune_index)
            # Small delay to debounce the button press
            Ed.TimeWait(200, Ed.TIME_MILLISECONDS)
        elif key_pressed == Ed.KEYPAD_TRIANGLE:
            # Replay current tune
            Ed.PlayBeep() # Single beep to indicate replay
            play_current_tune(current_tune_index)
            Ed.TimeWait(200, Ed.TIME_MILLISECONDS)
        else:
            # If no button pressed, and music ended, just replay the current tune
            play_current_tune(current_tune_index)
    
    # A small delay to prevent the loop from running too fast
    Ed.TimeWait(10, Ed.TIME_MILLISECONDS)