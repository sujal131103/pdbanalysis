from pdb_io import read_atoms

models = read_atoms("6B1E.pdb")

print("Total Models:", len(models))

for model in models:
    print("\n==============================")
    print("Model ID:", model.id)
    print("Number of Chains:", len(model.chains))

    for chain in model.chains:
        print("\n  Chain ID:", chain.id)
        print("  Number of Residues:", len(chain.residues))

        for residue in chain.residues:
            print(
                "    Residue:",
                residue.resname,
                residue.resnum,
                "Chain:",
                residue.chain,
                "Atoms:",
                len(residue.atoms)
            )

            for atom in residue.atoms:
                print(
                    "      Atom:",
                    atom.serial,
                    atom.name,
                    "Res:",
                    atom.resname,
                    atom.resnum,
                    "Chain:",
                    atom.chain,
                    "Coords:",
                    f"({atom.x:.3f}, {atom.y:.3f}, {atom.z:.3f})",
                    "B-factor:",
                    atom.bfactor,
                    "Occupancy:",
                    atom.occup
                )
