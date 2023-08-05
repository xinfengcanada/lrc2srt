#!/usr/bin/env python

# a script can help u to convert the lyrics file to .srt
# created by wOOL, iamwool@gmail.com
# edited by eadmaster  http://eadmaster.tk

import sys
import re
import os
from datetime import datetime
from datetime import timedelta
from tkinter.filedialog import *

p = re.compile("[0-9]+")
filename = askopenfilename(
    initialdir='/home/dd/Desktop/test_project/lrc2srt')
print(filename)

lrc = open(filename, encoding='utf-8')
listtime = []
listlyrics = []

for line in lrc.readlines():
    if p.match(line.split(":")[0].replace("[", "")):
        listtime.append("00:" + line.split("]")[0].replace("[", "")+"0")
        listlyrics.append(line.split("]")[1])

# read file and delete empty&useless lines

o = ""
i = 0
# listtime[i].replace(".",",")+\
while i <= listtime.__len__()-2:
    start_time = (datetime.strptime(
        listtime[i], "%H:%M:%S.%f")-datetime.strptime("1", "%S"))
    if (start_time.days < 0):
        start_time = (datetime.strptime(
            listtime[i], "%H:%M:%S.%f")-datetime.strptime("0", "%S"))
    if (start_time.microseconds == 0):
        # add 1 msec to avoid empty msec field
        start_time = start_time+timedelta(microseconds=1)

    o = o +\
        str(i+1) +\
        "\n" +\
        "0" + str(start_time).replace("000", "").replace(".", ",") +\
        " --> " +\
        listtime[i+1].replace(".", ",") +\
        "\n"+listlyrics[i] +\
        "\n"
    i = i+1

o = o + str(i+1) + "\n" + listtime[-1].replace(".",
                                               ",") + " --> " + "\n" + listlyrics[-1] + "\n"
srt = open(filename.replace(".lrc", ".srt"), "w")
srt.write(o)
