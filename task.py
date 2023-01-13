from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""user give phone brand name as a input"""

def scrap(name):

    """chrome for testing"""
    driver = webdriver.Chrome()


    """create dynamic url by the help of user input"""
    source = f"https://www.amazon.in/s?k=%7B{name}%7D&page=1&crid=1PO2HKUPJL10Y&qid=1673608592&sprefix=sa%2Caps%2C1050&ref=sr_pg_1"

    driver.get(source)

    """empty list to store dictionaries"""
    final_data =[]

    """to get phone object by this"""

    phones = driver.find_elements(By.XPATH,"//div[@class ='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border']")

    print(f"here are some of {name} products for you" )

    print(len(phones))
    for pr in phones:
        
        """to get phone name """
        phonename =  pr.find_element(By.TAG_NAME, "h2").text

        user_input = str(name).lower()
        phone_name = phonename.lower()

     
        if user_input in phone_name:
            
            """to get phone price"""
            phone_price = pr.find_element(By.CLASS_NAME, 'a-price-whole').text

            if phone_price is None:

                phoneprice = "not available"

            else:

                phoneprice = phone_price    

            """store data in dictionary"""
            final_data.append({
                "phone_name":phone_name,
                "phone_price":phoneprice  
            })
        
        else:

            continue


    for data in final_data:

        print(data)

    # link = driver.find_element(By.XPATH,'//a[@class= "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    # link.click()
    
    # links.append(link)



    while True:

        pass

scrap("mi")

"""from requests_html import HTMLSession
from bs4 import BeautifulSoup


s = HTMLSession()



def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.co.in' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return


while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)"""



