

'''residues = read_pdb("6B1E.pdb")

print("Total residues:", len(residues))
print("\nFirst residue atoms:")
for atom in residues[1]:
    print(atom)'''

from pdb_io import read_pdb

residues = read_pdb("6B1E.pdb")
print(residues[2:5])
print("Total residues:", len(residues))

residue1 = residues[2]
residue2 = residues[45]

min_dist = residue1.minimum_distance(residue2)
print("Minimum distance between residue 2 and 50:", min_dist)

for chain in chain :
    for residue in chain.residue:
        print (residue)