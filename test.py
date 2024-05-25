import src.commprs_core as comm
import unittest


class commTest(unittest.TestCase):
    def test_runCommand(self):
        self.assertEqual(comm.runCommand("sum", ["12", "13"]), 25)

    def test_runFirst(self):
        self.assertEqual(comm.runFirst("sum(12, 13)"), 25)

    def test_runAll_MultiCommands(self):
        self.assertEqual(list(comm.runAll("sum(12, 13);mul(1, 2)")), [25, 2])

    def test_runFirst_NestedComs(self):
        self.assertEqual(comm.runFirst("sum(mul(2,6), 13)"), 25)

    def test_runAll_VarDefine(self):
        self.assertEqual(list(comm.runAll("$x = 12;x")), [None, 12])

    def test_runAll_VarUse(self):
        self.assertEqual(list(comm.runAll("$x = 12;sum(x,sum(x,2))")), [None, 26])

    def test_runAll_PluseOperator(self):
        self.assertEqual(list(comm.runAll("$x = 1+2; mul(x + 2,5)")), [None, 25])

if __name__ == "__main__":
    unittest.main()
