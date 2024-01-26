#%%
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def diamond_tessellation(rows, cols):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    for row in range(rows):
        for col in range(cols):
            diamond = patches.Polygon([
                (col + 0.5, row), 
                (col + 1, row + 0.5), 
                (col + 0.5, row + 1), 
                (col, row + 0.5)
                ], edgecolor='grey', facecolor='whitesmoke')
            ax.add_patch(diamond)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    plt.show()

#%%

diamond_tessellation(2, 9)  # 4 rows and 5 columns