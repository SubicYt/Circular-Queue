import unittest
from circularqueue import *

class TestCircularQueue(unittest.TestCase):
    def test_init_empty(self):
        CQ1 = CircularQueue()
        self.assertEqual(len(CQ1), 0)
    
    def test_init_with_processes(self):
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        self.assertEqual(CQ1._head.pid, "send_mail")

    def test_add_process_one(self):
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        
        self.assertEqual(CQ1._head.pid, "send_mail")
        p4 = Process("HEKL",90)

        CQ1.add_process(p4)
        self.assertEqual(CQ1._head.prev.pid, "HEKL")
    
    def test_add_process_two(self):
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        
        self.assertEqual(CQ1._head.pid, "send_mail")

        p4 = Process("HEKL",90)
        p5 = Process("HHH")
        
        newProcesses = [p4, p5]
        for items in newProcesses:
            CQ1.add_process(items)

        self.assertEqual(CQ1._head.prev.pid, "HHH")

    def test_add_processes_three(self):
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        
        self.assertEqual(CQ1._head.pid, "send_mail")

        p4 = Process("HEKL",90)
        p5 = Process("HHH")
        p6 = Process("Hello world")
        newProcesses = [p4, p5, p6]
        for items in newProcesses:
            CQ1.add_process(items)

        self.assertEqual(CQ1._head.prev.pid, "Hello world")
        self.assertEqual(CQ1._head.prev.cycles, 100)

    def test_repr(self):
        pass

    def test_remove_process_3_middle(self):
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        
        self.assertEqual(CQ1._head.pid, "send_mail")

        p4 = Process("HEKL",90)
        p5 = Process("HHH")
        p6 = Process("Hello world")
        newProcesses = [p4, p5, p6]
        for items in newProcesses:
            CQ1.add_process(items)
        
        CQ1.remove_process(p6)
        self.assertEqual(CQ1._head.prev.pid, "HHH")
        self.assertEqual(len(CQ1), 5)
    
    def test_remove_process_2_middle(self):
        """TODO: implement this"""
        
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        
        self.assertEqual(CQ1._head.pid, "send_mail")

        p4 = Process("HEKL",90)
        p5 = Process("HHH")
        p6 = Process("Hello world")
        newProcesses = [p4, p5, p6]
        for items in newProcesses:
            CQ1.add_process(items)
        
        CQ1.remove_process(p5)
        self.assertEqual(CQ1._head.prev.pid, "Hello world")
        self.assertEqual(len(CQ1), 5)

    def test_remove_process_3_head(self):
        """TODO: implement this"""
        
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        
        self.assertEqual(CQ1._head.pid, "send_mail")

        p4 = Process("HEKL",90)
        p5 = Process("HHH")
        p6 = Process("Hello world")
        newProcesses = [p4, p5, p6]
        for items in newProcesses:
            CQ1.add_process(items)
        
        CQ1.remove_process(p1)
        self.assertEqual(CQ1._head.pid, "create_password")
        self.assertEqual(len(CQ1), 5)
    
    def test_remove_process_3_final(self):
        """TODO: implement this"""
        
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        
        self.assertEqual(CQ1._head.pid, "send_mail")

        p4 = Process("HEKL", 90)
        p5 = Process("HHH")
        p6 = Process("Hello world")
        newProcesses = [p4, p5, p6]

        for process in newProcesses:
            CQ1.add_process(process)
        
        for process in items:
            CQ1.remove_process(process)

        self.assertEqual(CQ1._head.pid, "HEKL")
        self.assertEqual(len(CQ1), 3)

    def test_remove_process_1(self):
        pass
    #reference previous test cases

    def test_kill_3_middle(self):
        pass

    def test_add_process(self):
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        self.assertEqual(CQ1._head.pid, "send_mail")

        CQ1.add_process(Process("Get_hello", 6000))
        self.assertEqual(CQ1._head.prev.pid, "Get_hello")
        self.assertEqual(CQ1._head.prev.prev.pid, "get_login")
        self.assertEqual(CQ1._head.link.pid, "create_password")

    
    def test_remove_process(self):
        p1 = Process("send_mail", 5)
        p2 = Process("create_password", 3000)
        p3 = Process("get_login", 5000)

        items = [p1, p2, p3]
        CQ1 = CircularQueue(items)
        self.assertEqual(CQ1._head.pid, "send_mail")
        p4 = Process("Get_hello", 6000)
        CQ1.add_process(p4)

        self.assertEqual(CQ1._head.prev.pid, "Get_hello")
        self.assertEqual(CQ1._head.prev.prev.pid, "get_login")
        self.assertEqual(CQ1._head.link.pid, "create_password")

        CQ1.remove_process(p1)
        self.assertEqual(CQ1._head.pid, "create_password")

        CQ1.remove_process(p2)
        self.assertEqual(CQ1._head.pid, "get_login")
if __name__ == "__main__":
    
    unittest.main() 
