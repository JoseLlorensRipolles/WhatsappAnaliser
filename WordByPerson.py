import sys
import re
import matplotlib.pyplot as plt


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        return int(round(pct * total)/100)

    return my_autopct

if __name__ == "__main__":
    key_word = sys.argv[1]
    f = open("Resources/chat.txt", "r", encoding="utf8")
    text = f.read()
    lines = text.splitlines()
    n_msg_for_person = {}
    for line in lines:
        try:
            name = re.search('^(\d+)/(\d+)/(\d+), (\d+):(\d+) - (.+):', line).group(6)
            # FIX THIS
            if ':' not in name:
                words_in_line = line.split()
                for word_in_line in words_in_line:
                    if key_word == word_in_line:
                        try:
                            n_msg_for_person[name] += 1
                        except KeyError:
                            n_msg_for_person[name] = 1
            else:
                pass
        except AttributeError:
            pass
    print(n_msg_for_person)

    labels = n_msg_for_person.keys()
    values = []

    for label in labels:
        values.append(n_msg_for_person[label])

    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, startangle=90, autopct=make_autopct(values))
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('# of "' + key_word + '" by person')
    plt.show()
