from sele import webdriver
import time
from selenium.webdriver.common.keys import Keys
web=webdriver.Chrome()
web.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458755421&hvpos=&hvnetw=g&hvrand=14368195969448560225&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9301104&hvtargid=kwd-10573980&hydadcr=14453_2154373")
time.sleep(1)

login=web.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/form/div[1]/div[1]/span/div[1]/input")
login.send_keys("1234567890")

Submit=web.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/form/div[3]/div/span/span/input")
Submit.click()