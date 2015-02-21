import time
import fluidsynth

fs = fluidsynth.Synth(polyphony=128, channels=16)
fs.start(driver="pulseaudio")
## Your installation of FluidSynth may require a different driver.
## Use something like:
# fs.start(driver="pulseaudio") or fs.start(driver="alsa")

sfid = fs.sfload("/usr/share/sounds/sf2/TimGM6mb.sf2")

preset = 19
bank = 0

fs.program_select(0, sfid, bank, preset)
fs.noteon(0, 60, 80)
fs.noteon(0, 67, 80)
fs.noteon(0, 76, 80)

insts = fs.get_instrument_list(sfid)

print "Playing " + insts[str(bank).zfill(3) + '-' + str(preset).zfill(3)]

print "Active voices: " + str(fs.count_active_voices())
time.sleep(1.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

print "Active voices: " + str(fs.count_active_voices())

fs.delete()
