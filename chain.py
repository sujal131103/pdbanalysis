class Chain:
    def __init__(self, chain_id):
        self.id = chain_id
        self.residues = []

    def add_residue(self, residue):
        self.residues.append(residue)

    def minimum_distance(self, other_chain):
        min_dist=None
        for res1 in self.residues:
            for res2 in other_chain.residues:
                dist = res1.minimum_distance(res2)
                if min_dist is None:
                    min_dist= dist
                    continue
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    def __repr__(self):
        return f"<Chain {self.id}, Residues={len(self.residues)}>"
        