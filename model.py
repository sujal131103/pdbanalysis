import re

class Model:
    def _init_(self):
        self.id = None
        self.chains = {}

    def set_data(self, line):
        if line.startswith("MODEL"):
            self.id = int(line.split()[1])

    def add_chain(self, chain):
        self.chains[chain.id] = chain

    def _repr_(self):
        return f"<Model id={self.id}, NumChains={len(self.chains)}>"