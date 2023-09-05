# main.py
from mpi4py import MPI
import pandas as pd
from my_plotting_functions import plotScatterMatrix

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load data for df1 and df2 (or distribute the data as needed)
if rank == 0:
    # Load df1 as an argument
    nRowsRead = 1000 # specify 'None' if want to read whole file
    # PS_20174392719_1491204439457_log.csv may have more rows in reality, but we are only loading/previewing the first 1000 rows
    df1 = pd.read_csv('./archive/PS_20174392719_1491204439457_log.csv', delimiter=',', nrows = nRowsRead)
    df1.dataframeName = 'PS_20174392719_1491204439457_log.csv'
    nRow, nCol = df1.shape
    print(f'There are {nRow} rows and {nCol} columns')
    selected_columns = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFraud']
    plotScatterMatrix(df1, selected_columns)
else:
    df1 = None

if rank == 1:
    # Load df2 data
    batch_size = 1000
    start_row = 1000  # Start from row 1000 (change this as needed)

    # Load the next batch of rows
    df2 = pd.read_csv('./archive/PS_20174392719_1491204439457_log.csv', delimiter=',', skiprows=range(1, start_row + 1), nrows=batch_size)
    selected_columns = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFraud']
    plotScatterMatrix(df2, selected_columns)
else:
    df2 = None

# Broadcast data to all processes
df1 = comm.bcast(df1, root=0)
df2 = comm.bcast(df2, root=1)
