import re
import matplotlib.pyplot as plt
from datetime import date
import time


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        return int(round(pct * total)/100)
    return my_autopct

if __name__ == "__main__":
    f = open("Resources/chat.txt", "r", encoding="utf8")
    text = f.read()
    lines = text.splitlines()
    n_msg_by_day = {}
    for line in lines:
        try:
            search = re.search('^(\d+)/(\d+)/(\d+), (\d+):(\d+) - (.+):', line)

            day = search.group(1)
            month = search.group(2)
            year = '20' + search.group(3)

            msg_date = date(int(year), int(month), int(day))
            # FIX THIS
            try:
                n_msg_by_day[msg_date] += 1
            except KeyError:
                n_msg_by_day[msg_date] = 1
        except AttributeError:
            pass
    labels = sorted(n_msg_by_day.keys())
    values = []
    for label in labels:
        values.append(n_msg_by_day[label])
    plt.plot(labels,values)
    plt.show()
