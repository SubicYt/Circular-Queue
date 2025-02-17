from process import *
class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""
    _head = Process
    _len = 0
    def __init__(self, processes = None):
        self._head = None
        self._len = 0
        self._d_processes = {}

        if processes is not None:
            for process in processes:
                self.add_process(process)
    def __repr__(self):
        if self._head == None:
            return ("Circular Queue")
        else:
            processes = []
            current = self._head
            while True:
                processes.append(f"Process({current.pid},{current.cycles})")
                current = current.link
                if current == self._head:
                    break

        return f"CircularQueue({', '.join(processes)})"

    def __len__(self):
        return self._len

    def add_process(self, item):
        """adds a process to the end of the circular queue"""
        self._d_processes[item.pid] = Process(item)
        if len(self) == 0:
            self._head = item
            self._head.link = self._head
            self._head.prev = self._head
        else:
            item.link = self._head
            item.prev = self._head.prev
            self._head.prev.link = item
            self._head.prev = item

        self._len +=1

    def remove_process(self, item):
        """removes process from circular queue"""
        Removeable_item= item

        del self._d_processes[item.pid]

        if len(self)==0:
            return RuntimeError("Cannot remove from empty list")
        
        elif self._head == self._head.prev:
            self._head = None
        
        else:
            prevProcess = item.prev
            nextProcess = item.link
            prevProcess.link = nextProcess
            nextProcess.prev = prevProcess

            if item == self._head:
                self._head = nextProcess

        self._len -=1
        return Removeable_item

    def kill(self, pid:str):
        if pid not in self._d_processes:
            raise KeyError(f"Process with '{pid}' not found")
        else:
            process = self._d_processes[pid]
            self.remove_process(process)
            return process    


    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []   # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link
            
            n_remaining -= 1

        return '\n'.join(return_strings)
