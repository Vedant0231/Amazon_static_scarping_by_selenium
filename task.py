from selenium  import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""user will enter brand name as a input"""
name = input("enter you specific brand:   ")

"""user will enter specific page numbers they want to scrape"""
pages = int(input("enter specific page number you want to scrape(between 1 to 20):    "))


"""chrome for testing"""
driver = webdriver.Chrome()

""" store products data here """
final_data=[]

for i in range(1,pages):   

    source = (f"https://www.amazon.in/s?k={name}&page={i}")

    driver.get(source)
     
    """path of div where products data are present"""    
    products = driver.find_elements(By.XPATH,"//div[@class ='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border']")

    for pr in products:
        
        """to get phone name """
        productname =  pr.find_element(By.TAG_NAME, "h2").text

        user_input = str(name).lower()
        product_name = productname.lower()

        """we are doing this because we to filter products to get only the brand specific products"""
        if user_input in product_name:
            
            """to get phone price"""

            """check price is present or not""" 
            try:
                product_price = pr.find_element(By.CLASS_NAME, 'a-price').text
            """if price is not present then product_price will give "not found" as return"""
            except:
                product_price = "not found"     

            """store data in dictionary"""
            final_data.append({
                "product_name":product_name,
                "product_price":product_price  
            })

for data in final_data:

    print(data)    


