import unittest
import commprs_core as comm


class commTest (unittest.TestCase):
    def test_runCommand(self):
        self.assertEqual(comm.runCommand("sum", ['12', '13']), 25)

if __name__ == '__main__':
    unittest.main()