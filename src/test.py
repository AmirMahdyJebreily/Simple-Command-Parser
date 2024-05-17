import unittest
import commprs_core as comm


class commTest(unittest.TestCase):
    def test_runCommand(self):
        self.assertEqual(comm.runCommand("sum", ["12", "13"]), 25)

    def test_runFirst(self):
        self.assertEqual(comm.runFirst("sum(12, 13)"), 25)

    def test_runAll_MultiCommands(self):
        self.assertEqual(list(comm.runAll("sum(12, 13);mul(1, 2)")), [25, 2])


if __name__ == "__main__":
    unittest.main()
