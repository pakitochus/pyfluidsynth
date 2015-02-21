"""
This test demonstrated the new functions and options implemented
in the class Synth.
"""
import time
import fluidsynth

# Create and start the synthesizer with the selected options.
fs = fluidsynth.Synth(gain=0.1, polyphony=64, channels=16)
fs.start(driver="pulseaudio")

# Test the get_gain and set a new gain:
print "Current gain: " + str(fs.get_gain())
fs.set_gain(0.3)
print "Updated gain: " + str(fs.get_gain())

# Load a soundfont.
sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")

preset = 19
bank = 0
channel = 0

# Select the program and play a chord.
fs.program_select(channel, sfid, bank, preset)
fs.noteon(0, 60, 80)
fs.noteon(0, 67, 80)
fs.noteon(0, 76, 80)

# This way we check the information of the instrument loaded in a certain channel
information = fs.get_channel_info(channel)
bank = information.bank
preset = information.program

# We present the name of the instrument loaded using the instrument list
insts = fs.get_instrument_list(sfid)
print "Playing " + insts[str(bank).zfill(3) + '-' + str(preset).zfill(3)]

# Count the number of active voices
print "Active voices: " + str(fs.count_active_voices())

time.sleep(1.0)

# Stop the active chord
fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

# Print the nubmer of active voices (after stopping the notes)
print "Active voices: " + str(fs.count_active_voices())

fs.delete()
