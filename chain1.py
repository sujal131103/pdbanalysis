class Chain:
    def __init__(self):
        self.id = None
        self.residues = []

    def set_data(self, pdb_line):
        self.id = pdb_line[21]

    def __repr__(self):
        return f"<Chain={self.id}, NumRes={len(self.residues)}"