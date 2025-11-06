from atom import Atom
from residue import Residue

def read_pdb(filename):
    residue_list = []
    current_residue = []
    prev_resid = None
    prev_chain = None

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(("ATOM", "HETATM")):
                atom = Atom()
                atom.set_data(line)
                if prev_resid is None:
                    prev_resid = atom.resnum
                    prev_chain = atom.chain
                    current_residue = Residue()
                    current_residue.set_data(line)
                    current_residue.atoms.append(atom)
                    residue_list.append(current_residue)
                else:
                    if atom.resnum == prev_resid and atom.chain == prev_chain:
                        current_residue.atoms.append(atom)
                    else:
                        current_residue = Residue()
                        current_residue.set_data(line)
                        residue_list.append(current_residue)
                        current_residue.atoms.append(atom)
                        prev_resid = atom.resid
                        prev_chain = atom.chain

    return residue_list
