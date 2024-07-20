import matplotlib.pyplot as plt
import numpy as np

# Data from the Excel file
data = {
    "Population": ["M 18 - 24", "M 25 - 39", "M 40 - 59", "M 60 - 80", "W 18 - 24", "W 25 - 39", "W 40 - 59", "W 60 - 80"],
    "Posts": [354, 489, 412, 192, 167, 241, 104, 58],
    "Unique Users": [25, 35, 30, 14, 18, 21, 9, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a pie chart
fig, ax = plt.subplots()
colors = plt.cm.tab20.colors
wedges, texts, autotexts = ax.pie(df['Unique Users'], labels=df['Population'], autopct='%1.1f%%', startangle=90, colors=colors, textprops=dict(color="w"))

# Adjust text placement
for text, autotext in zip(texts, autotexts):
    text.set_fontsize(10)
    autotext.set_fontsize(8)
    if float(autotext.get_text().strip('%')) < 5:
        if float(autotext.get_text().strip('%')) == 4.0:
            autotext.set_position((0, 0))  # Place the 4% label inside its section
            autotext.set_fontsize(10)
        else:
            text.set_position((1.1, 1.1))  # Move the label outside if the percentage is too small
            autotext.set_position((1.3, 1.3))  # Move the percentage outside with a line pointing

# Draw lines for small percentages
for i, p in enumerate(wedges):
    if float(autotexts[i].get_text().strip('%')) < 5 and float(autotexts[i].get_text().strip('%')) != 4.0:
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        x = np.cos(np.deg2rad(ang))
        y = np.sin(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        ax.annotate(df['Unique Users'][i],
                    xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, fontsize=10,
                    arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle))

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a title
plt.title('Distribution of Unique Users in SMHD Dataset by Age and Gender')

# Add a legend
legend_labels = df['Population']
ax.legend(wedges, legend_labels, title="Subpopulations", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Save the plot
file_path = '/mnt/data/subpopulations_pie_chart_with_legend_final_fixed.png'
plt.savefig(file_path, bbox_inches="tight")

# Display the plot
plt.show()

file_path
