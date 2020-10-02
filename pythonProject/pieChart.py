import matplotlib.pyplot as plt

labels = 'cool', 'very cool', 'awesome'
sizes = [492, 50, 2]
colors = ['gold', 'yellow', 'coral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.show()

