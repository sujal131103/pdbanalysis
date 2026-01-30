from atom import Atom
from residue import Residue
from chain1 import Chain
from model import Model

def create_res_id(resname, resnum, chain):
    return f"{resname}{resnum}{chain}"

def read_atoms(filename):
    models = []
    curr_model = None
    curr_chain = None
    curr_residue = None

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if not line:
                continue

            
            if line.startswith("MODEL"):
                curr_model = Model()
                curr_model.set_data(line)
                curr_model.chains = []
                models.append(curr_model)
                curr_chain = None
                curr_residue = None
                continue

           
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # For PDBs without MODEL record
                if curr_model is None:
                    curr_model = Model()
                    curr_model.id = 1
                    curr_model.chains = []
                    models.append(curr_model)

                atom = Atom()
                atom.set_data(line)

                chain_id = atom.chain
                res_id = create_res_id(atom.resname, atom.resnum, chain_id)

                
                if curr_chain is None or curr_chain.id != chain_id:
                    curr_chain = Chain()
                    curr_chain.set_data(line)
                    curr_chain.residues = []
                    curr_model.chains.append(curr_chain)
                    curr_residue = None

               
                if curr_residue is None or curr_residue.id != res_id:
                    curr_residue = Residue()
                    curr_residue.set_data(line)
                    curr_residue.atoms = []
                    curr_chain.residues.append(curr_residue)

                
                curr_residue.atoms.append(atom)

    return models