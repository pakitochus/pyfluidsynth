import fluidsynth
import time
from pyalsa.alsaseq import *

# Start the midi alsa-Seq to connect ports.
sequencer = Sequencer(name = 'default',
                      clientname = 'aconnect.py',
                      streams = SEQ_OPEN_DUPLEX,
                      mode = SEQ_BLOCK)

# Create and start the synthesizer with the selected options.
fs = fluidsynth.Synth(gain=0.1, polyphony=96, channels=16)
fs.start(audiodriver='alsa')
fs.start_midi()  # Default is alsa_seq

# Test the get_gain and set a new gain:
print "Current gain: " + str(fs.get_gain())
fs.set_gain(0.3)
print "Updated gain: " + str(fs.get_gain())

# Load a soundfont.
#sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")
sfid = fs.sfload("/home/pi/chusynth/pyfluidsynth/test/ChusoCol2.sf2")
#sfid = fs.sfload("/home/pakitochus/Software/Musica/Soundfont/ChusoCol2.sf2")

preset = 50
bank = 0
channel = 0

connectionlist = sequencer.connection_list()
sender = (20,0)
exclusive = 0
convert_time = 0
convert_real = 0
queue = 0
# Locate Fluidsynth and set the destination port.
for el in connectionlist:
#    print el
    if 'FLUID' in el[0]:
        dest = (el[1],0)
        print 'Connected to ' + el[0]
sequencer.connect_ports(sender, dest, queue, exclusive, convert_time, convert_real)

# Select the program and play a chord.
fs.program_select(channel, sfid, bank, 0)
print "now you can play a few notes in piano"
time.sleep(20.0)
inst = fs.get_instrument_list(sfid)
print "now you can play a few more notes in "+inst[str(bank).zfill(3)+'-'+str(preset).zfill(3)]
fs.program_select(channel, sfid, bank, preset)
time.sleep(10.0)

print "stopping..."
fs.stop_midi()
fs.delete()
