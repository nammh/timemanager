import os
import sys
import time
import datetime

import pandas as pd
import matplotlib.pyplot as plt

def load():
    data = pd.read_csv("./timeline.csv", parse_dates=["start", "end"])
    data["day"] = data["start"]
    data["day"] = data["day"].apply(lambda x: x.date())
    return data

def today(data):
    today = (data.loc[data["day"] == datetime.datetime.now().date])
    return today

def datetime2float(_dt_obj):
    dt_str = _dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    t_obj = time.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    return time.mktime(t_obj)

def datetime2datestr(_dt_obj):
    return _dt_obj.strftime("%Y-%m-%d")

def datetime2timestr(_dt_obj):
    return _dt_obj.strftime("%H:%M:%S")

def plot_today():
    with plt.xkcd():
        data = load()
        data_today = today(data)
        events = list(set(data["task"]))
        events.sort()
        colors = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33','#a65628','#f781bf','#999999']

        start = datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")
        start = time.strptime(start, "%Y-%m-%d %H:%M:%S")
        start = time.mktime(start)
        xticks = [start + x*60*60 for x in range(9, 24)]
        xticks_label = [str(x)+":00" for x in range(9, 24)]
        fig, ax = plt.subplots(figsize=(16,9))
        ax2 = ax.twinx()
        cnt = 0
        for event in events:
            data_plt = (data.loc[data["task"] == event])
            starts = data_plt['start'].map(datetime2float)
            durations = data_plt['end'].map(datetime2float)\
                    - data_plt['start'].map(datetime2float)
            slices = [(starts[i],durations[i]) for i in durations.index]
            ax.broken_barh(slices, (4, 1), \
                    facecolors=colors[cnt%len(colors)], label=event)
            ax2.bar(xticks[cnt+3], sum(durations)/60., 60*60,\
                    color=colors[cnt%len(colors)], label=event, alpha=0.9)
            cnt+=1

        ax.set_yticks(range(10))
        ax2.set_yticks([x*30 for x in range(20)])
        ax.set_xticks(xticks)
        ax2.set_xticks(xticks)
        ax.set_xticklabels(xticks_label, rotation='vertical')
        ax2.set_xticklabels(xticks_label, rotation='vertical')
        ax.set_yticklabels([])
        ax2.set_yticklabels([x*30 for x in range(20)])
        ax.legend()
    plt.tight_layout()
    plt.show()

plot_today()
