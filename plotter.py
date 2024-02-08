import matplotlib.pyplot as plt
import numpy as np


def bar_chart(dict1,dict2,dict3,dict4,dict5):

    # Extract keys and values from dictionaries
    keys = list(dict1.keys())
    values1 = list(dict1.values())
    values2 = list(dict2.values())
    values3 = list(dict3.values())
    values4 = list(dict4.values())
    values5 = list(dict5.values())

    # Set the width of the bars
    bar_width = 0.25

    # Set the positions of the bars on the x-axis
    r1 = np.arange(len(keys))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width*2 for x in r1]
    r4 = [x + bar_width*3 for x in r1]
    r5 = [x + bar_width*4 for x in r1]

    # Plotting the bars
    plt.bar(r1, values1, color='r', width=bar_width, edgecolor='grey', label='NCD bz2')
    plt.bar(r2, values2, color='g', width=bar_width, edgecolor='grey', label='NCD lzma')
    plt.bar(r3, values3, color='b', width=bar_width, edgecolor='grey', label='NCD zlib')
    plt.bar(r4, values4, color='y', width=bar_width, edgecolor='grey', label='NGD')
    plt.bar(r5, values5, color='p', width=bar_width, edgecolor='grey', label='ALL')

    # Add xticks on the middle of the group bars
    plt.xlabel('Groups', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(keys))], keys)

    # Create legend & Show graphic
    plt.legend()
    plt.show()
