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
        self.chain = pdb_line[21].strip()

    def minimum_distance(self, otherRes):
        min_dist = float('inf')
        for a1 in self.atoms:
            for a2 in otherRes.atoms:
                d = a1.distance(a2)
                if d < min_dist:
                    min_dist = d
        return min_dist

    def __repr__(self):
        return f"<Residue name={self.resname}, num={self.resnum}, chain={self.chain}, numAtoms={len(self.atoms)}>"
