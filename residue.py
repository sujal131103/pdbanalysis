def create_res_id(resname, resnum, chain):
    return f"{resname}{resnum}{chain}"
class Residue:
    def __init__(self):
        self.id = None
        self.atoms = []
        self.resnum = None
        self.resname = None
        self.chain = None

    def set_data(self, pdb_line):
        self.resname = pdb_line[17:20].strip()
        self.resnum = pdb_line[22:26].strip()
        self.chain = pdb_line[21]
        self.id =  create_res_id(self.resname, self.resnum, self.chain)

    def minimum_distance(self, other):
        min_dist = float("inf")
        closest_pair = (None, None)
        for a1 in self.atoms:
            for a2 in other.atoms:
                d = a1.distance(a2)
                if d < min_dist:
                   min_dist = d
                   closest_pair = (a1, a2)
        return min_dist
                

    def __repr__(self):
        return f"<name={self.resname}, num={self.resnum}, chain={self.chain}, numAtoms = {len(self.atoms)}>"