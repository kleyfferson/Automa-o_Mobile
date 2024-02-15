import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


class TestSearchEvent(unittest.TestCase):
    def setUp(self) -> None:
        caps = {}
        caps["platformName"] = "Android"
        caps["appium:automationName"] = "uiautomator2"
        caps["appium:deviceName"] = "Android"
        caps["appium:appPackage"] = "br.com.drogasil"
        caps["appium:appActivity"] = "br.com.raiadrogasil.MainActivity"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        from appium.options.android import UiAutomator2Options        
        options = UiAutomator2Options()
        options.load_capabilities(caps)
        self.driver = webdriver.Remote("http://127.0.0.1:4723",  options=options)


    def tearDown(self) -> None:
        self.driver.quit()

    def test_pesquisainvalida(self) -> None:
        driver = self.driver
        self.driver.implicitly_wait(3)
        el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el1.click()
        el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Campo buscar produto")
        el1.click()
        el1.send_keys("####")  #digitando um produto invalido para fazer a pesquisa 
        el1 = driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.implicitly_wait(5)
        resultado = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")
        assert resultado.text == 'Os dados fornecidos são inválidos [RCHS-TCMPLT]' 


    def test_adicionarcarrinho_test(self) -> None:
        driver = self.driver
        self.driver.implicitly_wait(5)
        el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="categorias")
        el2.click()
        el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Selecionar categoria medicamentos")
        el3.click()
        el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Selecionar subcategoria medicamentos especiais")
        el4.click()
        el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Botão comprar")
        self.driver.implicitly_wait(5)
        el5.click()
        self.driver.implicitly_wait(5)
        el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Botão voltar")
        self.driver.implicitly_wait(5)   
        el6.click()
        self.driver.implicitly_wait(5)
        resultado = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"Acessar cesta de compras\"]/android.view.ViewGroup[2]/android.widget.TextView")
        assert resultado.text == '1' 
    
    def  test_pesquisavalida(self) -> None:
        driver = self.driver
        self.driver.implicitly_wait(5)
        el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Campo buscar produto")
        el2.click()
        el2.send_keys("dorflex")
        el2.click()
        el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView")
        el3.click()
        resultado = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Nome do produto")
        self.driver.implicitly_wait(5)
        assert resultado.text == 'Dorflex DIP Dipirona 1g 10 comprimidos' 

if __name__ == '__main__':
    unittest.main()