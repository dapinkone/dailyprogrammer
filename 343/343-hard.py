#!/usr/bin/python
# * generate sound data
# * serve the data over http, perhaps as a stream?
# * store music in music file format such as mp3/ogg
# * train a neural net or markov chain to generate similar sounds
#         to an input
# --------------------
# challenge recommendes an intermediate format for MIDI such as:
# 37 8.5 0.5
# 37 is the pitch
# 0.5 is the beats(length of sound)
# 8.5 is the starting beat.
# i'd rather use mp3/ogg though.
#####
import http.server
