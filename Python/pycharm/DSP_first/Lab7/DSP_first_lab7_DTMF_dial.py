# DTMF_dial: create a vector of tones correspond to Dual Tone Multi-frequency Dial phone numbers
# Usage: tones = DTMF_dial(phone numbers)
#        phone numbers = arbitrary phone number sequence range from '0' to '9', plus '*' and '#' symbols

import numpy as np
from numpy import cos, pi

def DTMF_dial(nums):
    tones = np.array([])     # create empty array to append tones vectors
    fs = 8000   # sampling frequency
    t_tone = 0.5    # tone length = 0.5sec
    nn = t_tone * fs    # number of samples collected during 0.5sec
    n1 = np.arange(0, nn, 1)
    t_pause = 0.1   # quiet period between each tone
    nn = t_pause * fs   # number of samples collected during 0.1sec
    n2 = np.arange(0, nn, 1)
    Amp = 1     # amplitude of the tone
    freq = np.array([[697, 770, 852, 941], [1209, 1336, 1477]])     # given
    for i in range(0, len(nums)):
        if nums[i] == '1':       # 1 = 697Hz + 1209Hz
            tone1 = Amp * cos(2*pi * freq[0][0]/fs * n1)    # 697Hz
            tone2 = Amp * cos(2*pi * freq[1][0]/fs * n1)    # 1209Hz
            tone3 = np.add(tone1, tone2)     # mix two frequency samples
            tones = np.hstack((tones, tone3))     # 0.5sec active button press period
            tone4 = 0 * cos(2*pi * 0/fs * n2)    # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))     # 0.1sec silent period
        elif nums[i] == '2':    # 2 = 697Hz + 1336Hz
            tone1 = Amp * cos(2 * pi * freq[0][0] / fs * n1)  # 697Hz
            tone2 = Amp * cos(2 * pi * freq[1][1] / fs * n1)  # 1336Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '3':    # 3 = 697Hz + 1477Hz
            tone1 = Amp * cos(2 * pi * freq[0][0] / fs * n1)  # 697Hz
            tone2 = Amp * cos(2 * pi * freq[1][2] / fs * n1)  # 1477Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '4':    # 4 = 770Hz + 1209Hz
            tone1 = Amp * cos(2 * pi * freq[0][1] / fs * n1)  # 770Hz
            tone2 = Amp * cos(2 * pi * freq[1][0] / fs * n1)  # 1209Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '5':    # 5 = 770Hz + 1336Hz
            tone1 = Amp * cos(2 * pi * freq[0][1] / fs * n1)  # 770Hz
            tone2 = Amp * cos(2 * pi * freq[1][1] / fs * n1)  # 1336Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '6':    # 6 = 770Hz + 1477Hz
            tone1 = Amp * cos(2 * pi * freq[0][1] / fs * n1)  # 770Hz
            tone2 = Amp * cos(2 * pi * freq[1][2] / fs * n1)  # 1477Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '7':   # 7 = 852Hz + 1209Hz
            tone1 = Amp * cos(2 * pi * freq[0][2] / fs * n1)  # 852Hz
            tone2 = Amp * cos(2 * pi * freq[1][0] / fs * n1)  # 1209Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '8':  # 8 = 852Hz + 1336Hz
            tone1 = Amp * cos(2 * pi * freq[0][2] / fs * n1)  # 852Hz
            tone2 = Amp * cos(2 * pi * freq[1][1] / fs * n1)  # 1336Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '9':  # 9 = 852Hz + 1477Hz
            tone1 = Amp * cos(2 * pi * freq[0][2] / fs * n1)  # 852Hz
            tone2 = Amp * cos(2 * pi * freq[1][2] / fs * n1)  # 1477Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '*':  # * = 941Hz + 1209Hz
            tone1 = Amp * cos(2 * pi * freq[0][3] / fs * n1)  # 941Hz
            tone2 = Amp * cos(2 * pi * freq[1][0] / fs * n1)  # 1209Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '0':  # 0 = 941Hz + 1336Hz
            tone1 = Amp * cos(2 * pi * freq[0][3] / fs * n1)  # 941Hz
            tone2 = Amp * cos(2 * pi * freq[1][1] / fs * n1)  # 1209Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
        elif nums[i] == '#':  # 0 = 941Hz + 1477Hz
            tone1 = Amp * cos(2 * pi * freq[0][3] / fs * n1)  # 941Hz
            tone2 = Amp * cos(2 * pi * freq[1][2] / fs * n1)  # 1477Hz
            tone3 = np.add(tone1, tone2)  # mix two frequency samples
            tones = np.hstack((tones, tone3))  # 0.5sec active button press period
            tone4 = 0 * cos(2 * pi * 0 / fs * n2)  # 0Hz; amplitude = 0
            tones = np.hstack((tones, tone4))  # 0.1sec silent period
    return tones, fs
