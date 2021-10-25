## To get values of html element attributes use ----> [ get_attributes() ]
Ref : https://www.youtube.com/watch?v=zxZkHl1dU0k

https://tor.stackexchange.com/questions/22354/python-selenium-with-tor-socks5-proxy

https://wkdtjsgur100.github.io/selenium-change-ip-en/


- In my case, the error was caused by the element I was looking for being inside an iframe. This meant I had to change frame before looking for the element:

```python
from selenium import webdriver
    
driver = webdriver.Chrome()
driver.get("https://www.google.co.uk/maps")

frame_0 = driver.find_element_by_class_name('widget-consent-frame')
driver.switch_to.frame(frame_0)

agree_btn_0 = driver.find_element_by_id('introAgreeButton')
agree_btn_0.click()
```
