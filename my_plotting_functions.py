# my_plotting_functions.py
import seaborn as sns
import matplotlib.pyplot as plt

def plotScatterMatrix(df, columns):
    df_selected = df[columns]
    g = sns.pairplot(df_selected)
    # Change the x-axis labels for specific columns
    new_labels = {
        'oldbalanceOrg': 'OldBalOrg',
        'newbalanceOrig': 'NewBalOrig',
        'oldbalanceDest': 'OldBalDest',
        'newbalanceDest': 'NewBalDest',
    }
    for i in range(len(columns)):
        for j in range(len(columns)):
            if i != j:
                ax = g.axes[i, j]
                ylabel = ax.get_ylabel()
                if ylabel in new_labels:
                    ax.set_ylabel(new_labels[ylabel])
    plt.subplots_adjust(bottom=0.07)  # Adjust the bottom margin here
    plt.show()
    pass