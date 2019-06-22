import matplotlib.pyplot as plott
squares=[1,4,9,16,25]
fig, ax= plott.subplots()
ax.plot(squares,linewidth=3)
#Label axes and set title for chart
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#Set tick label thickness
ax.tick_params(axis='both', labelsize=14)
plott.show()