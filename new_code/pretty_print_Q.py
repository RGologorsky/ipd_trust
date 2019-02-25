import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table

Q  = np.asarray([
            [
                "f(x1cc, y1cc)*p1cc*q1cc", \
                "f(x1cc, y1cc)*p1cc*(1 - q1cc)", \
                "f(x1cc, y1cc)*(1 - p1cc)*q1cc", \
                "f(x1cc, y1cc)*(1 - p1cc)*(1 - q1cc)", \
                "(1 - f(x1cc, y1cc))*p2cc* q2cc", \
                "(1 - f(x1cc, y1cc))*p2cc* (1 - q2cc)", \
                "(1 - f(x1cc, y1cc))* (1 - p2cc)*q2cc", \
                "(1 - f(x1cc, y1cc))* (1 - p2cc)* (1 - q2cc)" \
            ],

            [
                "f(x1cd, y1dc)*p1cd*q1dc", \
                "f(x1cd, y1dc)*p1cd*(1 - q1dc)", \
                "f(x1cd, y1dc)*(1 - p1cd)*q1dc", \
                "f(x1cd, y1dc)*(1 - p1cd)*(1 - q1dc)", \
                "(1 - f(x1cd, y1dc))*p2cd*q2dc", \
                "(1 - f(x1cd, y1dc))*p2cd*(1 - q2dc)", \
                "(1 - f(x1cd, y1dc))*(1 - p2cd)*q2dc", \
                "(1 - f(x1cd, y1dc))*(1 - p2cd)*(1 - q2dc)", \
            ],

            [
                "f(x1dc, y1cd)*p1dc*q1cd", \
                "f(x1dc, y1cd)*p1dc*(1 - q1cd)", \
                "f(x1dc, y1cd)* (1 - p1dc)*q1cd", \
                "f(x1dc, y1cd)*(1 - p1dc)*(1 - q1cd)", \
                "(1 - f(x1dc, y1cd))*p2dc*q2cd", \
                "(1 - f(x1dc, y1cd))*p2dc*(1 - q2cd)", \
                "(1 - f(x1dc, y1cd))*(1 - p2dc)* q2cd", \
                "(1 - f(x1dc, y1cd))*(1 - p2dc)*(1 - q2cd)", \
            ],

            [
                "f(x1dd, y1dd)*p1dd*q1dd", \
                "f(x1dd, y1dd)*p1dd*(1 - q1dd)", \
                "f(x1dd, y1dd)*(1 - p1dd)*q1dd", \
                "f(x1dd, y1dd)*(1 - p1dd)*(1 - q1dd)", \
                "(1 - f(x1dd, y1dd))*p2dd*q2dd", \
                "(1 - f(x1dd, y1dd))*p2dd*(1 - q2dd)", \
                "(1 - f(x1dd, y1dd))*(1 - p2dd)*q2dd", \
                "(1 - f(x1dd, y1dd))*(1 - p2dd)*(1 - q2dd)", \
            ],

            [
                "f(x2cc, y2cc)*p1cc*q1cc", \
                "f(x2cc, y2cc)*p1cc*(1 - q1cc)", \
                "f(x2cc, y2cc)*(1 - p1cc)*q1cc", \
                "f(x2cc, y2cc)*(1 - p1cc)*(1 - q1cc)", \
                "(1 - f(x2cc, y2cc))*p2cc* q2cc", \
                "(1 - f(x2cc, y2cc))*p2cc* (1 - q2cc)", \
                "(1 - f(x2cc, y2cc))* (1 - p2cc)*q2cc", \
                "(1 - f(x2cc, y2cc))* (1 - p2cc)* (1 - q2cc)", \
            ],

            [
                "f(x2cd, y2dc)*p1cd*q1dc", \
                "f(x2cd, y2dc)*p1cd*(1 - q1dc)", \
                "f(x2cd, y2dc)*(1 - p1cd)*q1dc", \
                "f(x2cd, y2dc)*(1 - p1cd)*(1 - q1dc)", \
                "(1 - f(x2cd, y2dc))*p2cd*q2dc", \
                "(1 - f(x2cd, y2dc))*p2cd*(1 - q2dc)", \
                "(1 - f(x2cd, y2dc))*(1 - p2cd)*q2dc", \
                "(1 - f(x2cd, y2dc))*(1 - p2cd)*(1 - q2dc)", \
            ],

            [
                "f(x2dc, y2cd)*p1dc*q1cd", \
                "f(x2dc, y2cd)*p1dc*(1 - q1cd)", \
                "f(x2dc, y2cd)* (1 - p1dc)*q1cd", \
                "f(x2dc, y2cd)*(1 - p1dc)*(1 - q1cd)", \
                "(1 - f(x2dc, y2cd))*p2dc*q2cd", \
                "(1 - f(x2dc, y2cd))*p2dc*(1 - q2cd)", \
                "(1 - f(x2dc, y2cd))*(1 - p2dc)* q2cd", \
                "(1 - f(x2dc, y2cd))*(1 - p2dc)*(1 - q2cd)", \
            ],

            [
                "f(x2dd, y2dd)*p1dd*q1dd", \
                "f(x2dd, y2dd)*p1dd*(1 - q1dd)", \
                "f(x2dd, y2dd)*(1 - p1dd)*q1dd", \
                "f(x2dd, y2dd)*(1 - p1dd)*(1 - q1dd)", \
                "(1 - f(x2dd, y2dd))*p2dd*q2dd", \
                "(1 - f(x2dd, y2dd))*p2dd*(1 - q2dd)", \
                "(1 - f(x2dd, y2dd))*(1 - p2dd)*q2dd", \
                "(1 - f(x2dd, y2dd))*(1 - p2dd)*(1 - q2dd)", \
            ]
        ])

Q_df = pd.DataFrame({
    #'1CC':Q[:,0],
    '1CD':Q[:,1],
    #'1DC':Q[:,2],
    #'1DD':Q[:,3],

    #'2CC':Q[:,4],
    #'2CD':Q[:,5],
    '2DC':Q[:,6],
    #'2DD':Q[:,7],
})

states = ["1CC", "1CD", "1DC", "1DD", "2CC", "2CD", "2DC", "2DD"]
Q_df.index = states
print(Q_df)

# ax = plt.subplot(111, frame_on=False) # no visible frame
# ax.xaxis.set_visible(False)  # hide the x axis
# ax.yaxis.set_visible(False)  # hide the y axis

# table(ax, Q_df)  # where df is your data frame

fig, ax = plt.subplots(figsize=(24, 24)) # set size frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
tabla = table(ax, Q_df, loc='upper right', colWidths=[.60]*len(Q_df.columns))  # where df is your data frame
tabla.auto_set_font_size(False) # Activate set fontsize manually
tabla.set_fontsize(10) # if ++fontsize is necessary ++colWidths
tabla.scale(1.2, 1.2) # change size table

plt.savefig('Q.png')