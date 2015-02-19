import time
import fluidsynth

fs = fluidsynth.Synth(polyphony=128,channels=16)
fs.start(driver="alsa")
## Your installation of FluidSynth may require a different driver.
## Use something like:
# fs.start(driver="pulseaudio")

sfid = fs.sfload("TimGM6mb.sf2")

fs.program_select(0, sfid, 0, 0)
fs.noteon(0, 60, 30)
fs.noteon(0, 67, 30)
fs.noteon(0, 76, 30)

stout = fs.get_instrument_list(1)
print stout

print fs.count_active_voices()
time.sleep(1.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()
