# advdependency_test.py

import unittest
from advdependency import FunctionalDependency, MultivaluedDependency, compute_fd_closure, decide_fd_implication, compute_mvd_closure, decide_mvd_implication

class TestDependencyAlgorithms(unittest.TestCase):
    def setUp(self):
        self.fd1 = FunctionalDependency(['A'], ['B'])
        self.fd2 = FunctionalDependency(['B'], ['C'])
        self.fd_set = [self.fd1, self.fd2]

        self.mvd1 = MultivaluedDependency(['A'], ['B'])
        self.mvd2 = MultivaluedDependency(['B'], ['C'])
        self.mvd_set = [self.mvd1, self.mvd2]

    def test_compute_fd_closure(self):
        closure = compute_fd_closure(self.fd_set, ['A'])
        self.assertEqual(closure, {'A', 'B', 'C'})

    def test_decide_fd_implication(self):
        fd = FunctionalDependency(['A'], ['C'])
        result = decide_fd_implication(self.fd_set, fd)
        self.assertTrue(result)

    def test_compute_mvd_closure(self):
        closure = compute_mvd_closure(self.mvd_set, ['A'])
        self.assertEqual(closure, {'A', 'B', 'C'})

    def test_decide_mvd_implication(self):
        mvd = MultivaluedDependency(['A'], ['C'])
        result = decide_mvd_implication(self.mvd_set, mvd)
        self.assertTrue(result)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDependencyAlgorithms('test_compute_fd_closure'))
    suite.addTest(TestDependencyAlgorithms('test_decide_fd_implication'))
    suite.addTest(TestDependencyAlgorithms('test_compute_mvd_closure'))
    suite.addTest(TestDependencyAlgorithms('test_decide_mvd_implication'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
