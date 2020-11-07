import unittest
import main
from testfunction import read_successful
from testfunction import sound_successful


class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(read_successful(main.inp), "read_succeed")
        self.assertEqual(sound_successful(main.out), "success")


if __name__ == '__main__':
    unittest.main()
    

