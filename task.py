from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""user give phone brand name as a input"""
name = input("enter phone brand name:  ")

"""chrome for testing"""
driver = webdriver.Chrome()

"""create dynamic url by the help of user input"""
source = f"https://www.amazon.in/s?k={name}&crid=1PO2HKUPJL10Y&sprefix=sa%2Caps%2C1050&ref=nb_sb_ss_ts-doa-p_1_2"

driver.get(source)

"""empty list to store dictionaries"""
final_data =[]

"""to get phone object by this"""

phones = driver.find_elements(By.XPATH,"//div[@class ='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border']")

print(f"here are some of {name} phones for you" )

print(len(phones))

for pr in phones:
    
    """to get phone name """
    phonename =  pr.find_element(By.TAG_NAME, "h2")
    
    """to get phone price"""
    phoneprice = pr.find_element(By.CLASS_NAME, 'a-price-whole')

    """store data in dictionary"""
    final_data.append({
        "phone_name":phonename.text,
        "phone_price":phoneprice.text
    })

for data in final_data:

    print(data)

while True:

    pass



 