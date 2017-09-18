import re
import matplotlib.pyplot as plt


def clean_text(text):
    clean_re = re.compile('\W+')
    return clean_re.sub(' ', text)


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        # return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
        return int(round(pct * total)/100)

    return my_autopct

if __name__ == "__main__" :
    f = open("Resources/chat.txt", "r", encoding="utf8")
    text = f.read()
    lines = text.strip().splitlines()
    n_lines = len(lines)
    first_day = lines[0][0:9]
    n_msg_for_person = {}
    pool_of_words = ['owel', 'awi', 'awii',]
    for line in lines:
        try:
            for word in pool_of_words:
                if word in line:
                    try:
                        n_msg_for_person[word] += 1
                    except KeyError:
                        n_msg_for_person[word] = 1
            else:
                pass
        except AttributeError:
            pass
    print(n_msg_for_person)

    labels = n_msg_for_person.keys()
    values = []
    for label in labels:
        values.append(n_msg_for_person[label])
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, startangle=90, autopct=make_autopct(values))



    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()