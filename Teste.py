from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

browser = webdriver.Chrome()


class TestTriangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser.get('http://www.vanilton.net/triangulo/#')

    def test_isosceles(self):

        browser.find_element(By.NAME, "V1").send_keys("4")
        browser.find_element(By.NAME, "V2").send_keys("4")
        browser.find_element(By.NAME, "V3").send_keys("1")
        browser.find_element(By.TAG_NAME, "input").submit()
        tipo_isosceles = browser.find_element(By.XPATH, "//div[4]")
        self.assertEqual(tipo_isosceles.text, "Isósceles", "A Aplicação não identificou o triangulo isósceles")


    def test_equilatero(self):

        browser.find_element(By.NAME, "V1").send_keys("6.2")
        browser.find_element(By.NAME, "V2").send_keys("6.2")
        browser.find_element(By.NAME, "V3").send_keys("6.2")
        browser.find_element(By.TAG_NAME, "input").submit()
        tipo_equilatero = browser.find_element(By.XPATH, "//div[4]")
        self.assertEqual(tipo_equilatero.text, "Equilátero", "A Aplicação não identificou o triangulo equilátero")


    def test_escaleno(self):

        browser.find_element(By.NAME, "V1").send_keys("3")
        browser.find_element(By.NAME, "V2").send_keys("4.1")
        browser.find_element(By.NAME, "V3").send_keys("5")
        browser.find_element(By.TAG_NAME, "input").submit()
        tipo_escaleno = browser.find_element(By.XPATH, "//div[4]")
        self.assertEqual(tipo_escaleno.text, "Escaleno", "A Aplicação não identificou o triangulo escaleno")

    def test_existence(self):

        browser.find_element(By.NAME, "V1").send_keys("0")
        browser.find_element(By.NAME, "V2").send_keys("1")
        browser.find_element(By.NAME, "V3").send_keys("0")
        browser.find_element(By.TAG_NAME, "input").submit()
        tipo_triagulo = browser.find_element(By.XPATH, "//div[4]")
        self.assertNotEqual(tipo_triagulo.text, "Escaleno", "A Aplicação não identificou que não é um triangulo")
        self.assertNotEqual(tipo_triagulo.text, "Equilátero", "A Aplicação não identificou que não é um triangulo")
        self.assertNotEqual(tipo_triagulo.text, "Isósceles", "A Aplicação não identificou que não é um triangulo")

    def test_no_number(self):

        browser.find_element(By.NAME, "V1").send_keys("a")
        browser.find_element(By.NAME, "V2").send_keys("a")
        browser.find_element(By.NAME, "V3").send_keys("a")
        browser.find_element(By.TAG_NAME, "input").submit()
        tipo_triagulo = browser.find_element(By.XPATH, "//div[4]")
        self.assertNotEquals(tipo_triagulo.text, "Equilátero", "A Aplicação não identificou que valor inserido não é numero")


    @classmethod
    def tearDownClass(cls):
        browser.close()
        browser.quit()


if __name__ == '__main__':
    unittest.main()