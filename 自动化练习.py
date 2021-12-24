# from selenium import webdriver
# import time
from selenium.webdriver import ActionChains
# cheomeDriver = webdriver.Edge(executable_path="D:\\edge浏览器驱动")#引用驱动器
# cheomeDriver.get("http://www.baidu.com")
# cheomeDriver.maximize_window()
# cheomeDriver.find_element_by_id("kw").send_keys("java")
# cheomeDriver.find_element_by_id("su").click()
# time.sleep(30)
# cheomeDriver.quit()


# from selenium import webdriver
# cheomeDriver = webdriver.Edge(executable_path="D://edge浏览器驱动.exe")
# cheomeDriver.get("https://product.suning.com/0000000000/12128129944.html#?safp=d488778a.13701.productWrap.2&safc=prd.0.0&safpn=10007&ch=cu")
# # cheomeDriver.maximize_window()
# # cheomeDriver.find_element_by_id("")
# cheomeDriver.find_element_by_xpath('//*[@id="colorItemList"]/dd/ul/li[3]/a/span')
# cheomeDriver.find_element_by_id("addCart").click()


# ****************国美***********************

from selenium import webdriver
cheomeDriver = webdriver.Edge(executable_path="D://edge浏览器驱动.exe")
cheomeDriver.get("https://www.gome.com.cn/")
ms=cheomeDriver.find_element_by_xpath('//*[@id="lisnav"]/li[1]/h3/a[1]')
ac=ActionChains(cheomeDriver)
ac.move_to_element(ms).perform()
cheomeDriver.find_element_by_xpath('//*[@id="lisnav"]/li[1]/h3/a[1]').click()

# sa=cheomeDriver.find_element_by_xpath('/html/body/div[2]/div[4]/ul/li[1]/div[2]')
# cc=ActionChains(cheomeDriver)
# cc.move_to_element(sa).perform()
# cheomeDriver.find_element_by_xpath('/html/body/div[2]/div[4]/ul/li[1]/div[2]').click()

# cheomeDriver.find_element_by_xpath("addCart").click()


# cheomeDriver.get("https://product.suning.com/0000000000/12128129944.html#?safp=d488778a.13701.productWrap.2&safc=prd.0.0&safpn=10007&ch=cu")
# # cheomeDriver.maximize_window()
# # cheomeDriver.find_element_by_id("")
# cheomeDriver.find_element_by_xpath('//*[@id="colorItemList"]/dd/ul/li[3]/a/span')
# cheomeDriver.find_element_by_id("addCart").click()
