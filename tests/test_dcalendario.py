import unittest
from dcalendario.dcalendario import criar_dcalendario

class TestDCalendario(unittest.TestCase):
    def test_criar_dcalendario(self):
        calendario = criar_dcalendario('2024-01-01', '2024-12-31')
        self.assertEqual(len(calendario), 366)  # Ano bissexto
        self.assertIn('AnoAtual', calendario.columns)

