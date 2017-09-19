import re
import matplotlib.pyplot as plt
import sys


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        return int(round(pct * total)/100)

    return my_autopct

if __name__ == "__main__":
    f = open("Resources/chat.txt", "r", encoding="utf8")
    text = f.read()
    lines = text.splitlines()
    n_of_word = {}
    pool_of_words = sys.argv[1:]
    for line in lines:
        try:
            for word_in_line in line.split():
                if word_in_line in pool_of_words:
                    try:
                        n_of_word[word_in_line] += 1
                    except KeyError:
                        n_of_word[word_in_line] = 1
            else:
                pass
        except AttributeError:
            pass

    labels = n_of_word.keys()
    values = []
    for label in labels:
        values.append(n_of_word[label])
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, startangle=90, autopct=make_autopct(values))
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
