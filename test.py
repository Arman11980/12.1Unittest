import unitest
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test walk method in runner
        :return
        """
        run = unitest.Runner("child")
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        """ Test run method in runner
        :return
        """
        run1 = unitest.Runner("Auto")
        for i in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    def test_challenge(self):
        """Test of two objects
        :return
        """
        run2 = unitest.Runner("man")
        run3 = unitest.Runner("bicycle")
        for i in range(10):
            run2.walk()
            run3.run()
        self.assertNotEqual(run2.distance, run3.distance)

if __name__ == '__main__':
    unittest.main
