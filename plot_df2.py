import pandas as pd
from my_plotting_functions import plotScatterMatrix

# Load df2 data
batch_size = 1000
start_row = 1000  # Start from row 1000 (change this as needed)
# Load the next batch of rows
df2 = pd.read_csv('./archive/PS_20174392719_1491204439457_log.csv', delimiter=',', skiprows=range(1, start_row + 1), nrows=batch_size)
selected_columns = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFraud']
plotScatterMatrix(df2, selected_columns)