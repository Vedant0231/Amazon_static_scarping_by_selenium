from selenium  import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

name = input("enter you specific brand:   ")

pages = int(input("enter specific page number you want to scrape(between 1 to 20):    "))


"""chrome for testing"""
driver = webdriver.Chrome()

final_data=[]

for i in range(1,pages):   

    source = (f"https://www.amazon.in/s?k={name}&page={i}")

    driver.get(source)

    phones = driver.find_elements(By.XPATH,"//div[@class ='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border']")

    for pr in phones:
        
        """to get phone name """
        phonename =  pr.find_element(By.TAG_NAME, "h2").text

        user_input = str(name).lower()
        phone_name = phonename.lower()

    
        if user_input in phone_name:
            
            """to get phone price"""

            try:
                phone_price = pr.find_element(By.CLASS_NAME, 'a-price').text

            except:
                phone_price = "not found"     

            """store data in dictionary"""
            final_data.append({
                "phone_name":phone_name,
                "phone_price":phone_price  
            })

for data in final_data:

    print(data)    


