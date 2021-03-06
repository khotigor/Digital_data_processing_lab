import math

DPI = 80
T_MATH = 0.1
T_BUILD = T_MATH * 0.005
AMPLITUDE = 1.4
BIAS = 0.5
FREQUENCY = 28076.17188
INITIAL_PHASE = 130
SAMPLING = 100000
NOISE_RATIO_SIGMA = 0.5

SNR = 13
A_NOISE = float(
    1.3 / (math.pow(10, (float(SNR) / 20))))  # root mean square of noise
