import re
import matplotlib.pyplot as plt



def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        return int(round(pct * total)/100)
    return my_autopct

if __name__ == "__main__":
    f = open("Resources/chat.txt", "r", encoding="utf8")
    text = f.read()
    lines = text.splitlines()
    n_msg_by_person = {}
    for line in lines:
        try:
            name = re.search('^(\d+)/(\d+)/(\d+), (\d+):(\d+) - (.+):', line).group(6)
            # FIX THIS
            if ':' not in name:
                try:
                    n_msg_by_person[name] += 1
                except KeyError:
                    n_msg_by_person[name] = 1
            else:
                pass
        except AttributeError:
            pass
    labels = n_msg_by_person.keys()
    values = []
    for label in labels:
        values.append(n_msg_by_person[label])
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, startangle=90, autopct=make_autopct(values))
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
