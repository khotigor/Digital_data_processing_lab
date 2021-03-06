import math
import random
import csv
import matplotlib.pyplot as plt
import numpy as np
from SignalClass import *
from values import *


# writer to csv
def write_to_csv(file_name, column_1, column_2):
    list_to_rev = [column_1, column_2]
    data_to_write = zip(*list_to_rev)

    points_file = open("{file_name}.csv".format(file_name=file_name), 'w')
    with points_file:
        writer = csv.writer(points_file)
        writer.writerows(data_to_write)
    print("Writing complete")


# read from cvs
def read_from_csv(file_name):
    with open("{file_name}.csv".format(file_name=file_name), "r") as f:
        reader = csv.reader(f)
        res = []
        for row in reader:
            res.append(row)
    return res


# creating a plotter for fft
def plotter_fft(dpi, arr_x, arr_y, title, x_label, y_label):
    plot = plt.figure(dpi=dpi, figsize=(1080 / dpi, 720 / dpi))
    plt.plot(arr_x, np.abs(arr_y) / 10000, linestyle='solid',
             label='a')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    return plot


# creating a plotter
def plotter(dpi, time_build, name, x_label, y_label, min_plt, max_plt):
    plot = plt.figure(dpi=dpi, figsize=(1080 / dpi, 720 / dpi))
    plt.axis([0, time_build, float(min_plt - 0.5), float(max_plt + 0.5)])

    plt.title(name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plot


# generate a random value of Normal distribution
def normal_random(noise_ratio_sigma):
    return random.normalvariate(0, noise_ratio_sigma)


# count cos of the signal
def signal_count(x, amplitude, frequency, init_phase, bias):
    new_cos_value = (
            amplitude * math.cos(2 * math.pi * x * frequency +
                                 math.pi * init_phase / 180) + bias)
    return new_cos_value


# count cos(0) of signal
def zero_signal(amplitude, frequency, init_phase, bias):
    return signal_count(0, amplitude, frequency, init_phase, bias)


# average of list
def avg_counter(list_in):
    return sum(list_in) / len(list_in)


# parser get i list from list of list
def parser(list_to_parse, num):
    res = []
    for list_from_list_to_parse in list_to_parse:
        res.append(float(list_from_list_to_parse[num]))
    return res
