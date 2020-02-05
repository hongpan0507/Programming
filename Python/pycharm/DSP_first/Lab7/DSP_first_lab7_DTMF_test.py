# DTMF_dial: create a vector of tones correspond to Dual Tone Multi-frequency Dial phone numbers
# Usage: tones = DTMF_dial(phone numbers)
#        phone numbers = arbitrary phone number sequence range from '0' to '9', plus '*' and '#' symbols

import numpy as np
from numpy import cos, pi
from DSP_first_lab7_DTMF_dial import *

v1 = DTMF_dial(['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#'])

print(v1)
