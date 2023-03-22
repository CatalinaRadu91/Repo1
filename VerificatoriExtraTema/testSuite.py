import unittest
from unittest import TestSuite, TestLoader

from HTMLTestRunner import HTMLTestRunner

from VerificatoriExtraTema.alert_tests import Alerts
from VerificatoriExtraTema.auth_test import Authentication
from VerificatoriExtraTema.context_menu_test import ContextMenu
from VerificatoriExtraTema.keys_tests import KeyPresses
from VerificatoriExtraTema.login_tests import LoginTC
from VerificatoriExtraTema.test_chrome import Chrome
from VerificatoriExtraTema.test_edge import Edge
from VerificatoriExtraTema.test_firefox import Firefox

# suita de teste = set de teste ce pot fi rulate in acelasi timp

class TestsSuite(unittest.TestCase):

    def test_suite(self):
        lista_teste = TestSuite()

        lista_teste.addTests([
            TestLoader().loadTestsFromTestCase(Alerts),
            TestLoader().loadTestsFromTestCase(Authentication),
            TestLoader().loadTestsFromTestCase(ContextMenu),
            TestLoader().loadTestsFromTestCase(KeyPresses),
            TestLoader().loadTestsFromTestCase(LoginTC),
            TestLoader().loadTestsFromTestCase(Chrome),
            TestLoader().loadTestsFromTestCase(Edge),
            TestLoader().loadTestsFromTestCase(Firefox),
        ])

        runner = HTMLTestRunner(
            title= 'Smoke Test',
            tested_by = 'Catalina',
            report_name= 'Tests Results'
        )

        runner.run(lista_teste)