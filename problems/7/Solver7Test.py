import unittest
from Solver7 import Solver7


# noinspection SpellCheckingInspection
class Solver7Test(unittest.TestCase):
    def test_count_test_ips(self):
        ip_file_name = 'test_input.txt'
        number_of_tls_ips = Solver7().count_ips_supporting_tls(ip_file_name)
        self.assertEqual(2, number_of_tls_ips)

    def test_count_problem_ips(self):
        ip_file_name = 'input.txt'
        number_of_tls_ips = Solver7().count_ips_supporting_tls(ip_file_name)
        self.assertEqual(105, number_of_tls_ips)

    def test_count_test_ips_ssl(self):
        ip_file_name = 'test_input_2.txt'
        number_of_tls_ips = Solver7().count_ips_supporting_ssl(ip_file_name)
        self.assertEqual(3, number_of_tls_ips)

    def test_count_problem_ips_ssl(self):
        ip_file_name = 'input.txt'
        number_of_tls_ips = Solver7().count_ips_supporting_ssl(ip_file_name)
        self.assertEqual(258, number_of_tls_ips)