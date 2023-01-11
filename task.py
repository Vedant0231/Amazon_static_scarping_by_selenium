from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def launchBrowser(phone_name):


   driver = webdriver.Chrome()
   source = f"https://www.amazon.in/s?k={phone_name}&crid=1PO2HKUPJL10Y&sprefix=sa%2Caps%2C1050&ref=nb_sb_ss_ts-doa-p_1_2"
   driver.get(source)

   """to get phone name"""
   phones_name = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
   
   for value in phones_name:
    
    phone_names = value.text

    print(phone_names)

   """to get phone price"""
   phones_price = driver.find_elements(By.XPATH, '//span[@class ="a-price-whole"]')

   for value in phones_price:

    phone_prices= value.text

    print(phone_prices)

   while(True):
   
       pass

launchBrowser("samsung")


"""xpaths"""
# //span[@class="a-size-medium a-color-base a-text-normal"] phone name

#//span[@class ="a-price-whole"]  phone price

#//div[@class = "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"]  phones object 
 