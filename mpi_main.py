from mpi4py import MPI
import pandas as pd
import subprocess

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load data for df1 and df2 (or distribute the data as needed)
if rank == 0:
    # Load df1 as an argument
    subprocess.call(["python", "plot_df1.py"])
elif rank == 1:
    # Load df2 data
    subprocess.call(["python", "plot_df1.py"])

