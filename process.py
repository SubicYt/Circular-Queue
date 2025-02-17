class Process:
    def __init__(self, pid:str, cycles = 100):
        self.pid = pid
        self.cycles = cycles
        self.link = None
        self.prev = None
    
    def __eq__(self, other):
        if self.pid == other.pid:
            return True
        else:
            return False
    
    def __repr__(self):
        return str((f"{self.pid}, {self.cycles}"))
    
