"""
This test demonstrated the new functions and options implemented
in the class Synth.
"""
import time
import fluidsynth
import os

os.nice(50)
# Create and start the synthesizer with the selected options.
fs = fluidsynth.Synth(gain=0.1, polyphony=2, channels=16)
fs.start(audiodriver="alsa")
fs.start_midi()  # Default is alsa_seq

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
fs.noteon(0, 60, 80)  # (Channel, note, velocity)
fs.noteon(0, 67, 80)
fs.noteon(0, 76, 80)  # We can't play that note, because polyphony=2, you should get an warning here

# This way we check the information of the instrument loaded in a certain channel
information = fs.get_channel_info(channel)
bank = information.bank
preset = information.program

# We present the name of the instrument loaded using the instrument list
insts = fs.get_instrument_list(sfid)
print "Playing " + insts[str(bank).zfill(3) + '-' + str(preset).zfill(3)]

# Count the number of active voices and CPU load
print "Active voices: " + str(fs.count_active_voices())
print "CPU load: " + "%0.2f" % (fs.get_cpu_load()) + "%"


# Augment the polyphony and play another note
fs.set_polyphony(128)
fs.noteon(0, 76, 80)
print "Active voices: " + str(fs.count_active_voices())
print "CPU load: " + "%0.2f" % (fs.get_cpu_load()) + "%"

time.sleep(1.0)

# Stop the active chord
fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(2.0)

# Print the number of active voices (after noteoff messages)
# Some voices might be still active
print "Active voices: " + str(fs.count_active_voices())
print "CPU load: " + "%0.2f" % (fs.get_cpu_load()) + "%"

fs.delete()
