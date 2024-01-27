from PyConSolv.ConfGen import PyConSolv
from PyConSolv.misc.analysis import Analysis
import subprocess

from PyConSolv.misc.mol2 import mol2Parser

if __name__ == '__main__':
    # print(subprocess.run(["source", "/home/rat/.bashrc"], shell=True))
    # print(subprocess.run(["/home/rat/PycharmProjects/setup_env.sh"], shell=True))
    # conf = PyConSolv('/home/rat/PYCONSOLV_DATA/ts/input.xyz')
    # conf.run(charge=0,  opt=False)

    residues = ['A', 'B']
    parser = mol2Parser('/home/rat/PYCONSOLV_DATA/ts/MCPB_setup',['{}x'.format(x) for x in residues])
    parser.writeCombinedMol2()


















# Import the necessary modules
import numpy as np
import pandas as pd
# from openbabel import openbabel

# Define a function to read an xmol file and return a pandas dataframe
def read_xmol(filename):
    # Open the file and read the first two lines
    with open(filename, "r") as f:
        natoms = int(f.readline().strip()) # Number of atoms
        comment = f.readline().strip() # Comment line
    # Read the rest of the file as a numpy array
    data = np.loadtxt(filename, skiprows=2)
    # Convert the array to a dataframe with columns for atom type, x, y, z
    df = pd.DataFrame(data, columns=["type", "x", "y", "z"])
    # Convert the atom type column to integer
    df["type"] = df["type"].astype(int)
    # Return the dataframe and the comment
    return df, comment

# Define a function to write a mol2 file from a pandas dataframe and a comment
def write_mol2(df, comment, filename):
    # Create an openbabel molecule object
    mol = openbabel.OBMol()
    # Loop over the rows of the dataframe and add atoms to the molecule
    for i, row in df.iterrows():
        # Create an openbabel atom object
        atom = openbabel.OBAtom()
        # Set the atomic number, coordinates, and index of the atom
        atom.SetAtomicNum(row["type"])
        atom.SetVector(row["x"], row["y"], row["z"])
        atom.SetIdx(i+1)
        # Add the atom to the molecule
        mol.AddAtom(atom)
    # Assign bond orders and aromaticity to the molecule
    mol.PerceiveBondOrders()
    mol.FindRingAtomsAndBonds()
    # Create an openbabel output stream
    out = openbabel.OBConversion()
    # Set the output format to mol2
    out.SetOutFormat("mol2")
    # Write the molecule to the file with the comment as the title
    out.WriteFile(mol, filename, comment)

# Example usage
# Read an xmol file
# df, comment = read_xmol("example.xmol")
# # Write a mol2 file
# write_mol2(df, comment, "example.mol2")