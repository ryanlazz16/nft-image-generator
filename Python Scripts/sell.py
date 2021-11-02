from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

TIME_FOR_USER_INTERACTIONS = 3600
TIME_FOR_PAGE_LOADS = 10
COLLECTION_NAME = 'digital-dialects'
NUMBER_NFTs = 7867

f = open('number.txt', 'r+')
START = int(f.read())

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

try:
	# login user
	driver.get('https://opensea.io/login?referrer=%2Faccount')
	xpath='//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li[2]/button'
	element = WebDriverWait(driver, TIME_FOR_PAGE_LOADS).until(lambda d: d.find_element(By.XPATH, xpath))
	element.click()

	# wait for successful login
	xpath='//*[@id="__next"]/div[1]/main/div/div/div[1]/div[3]/div[2]'
	element = WebDriverWait(driver, TIME_FOR_USER_INTERACTIONS).until(lambda d: d.find_element(By.XPATH, xpath))
except:
	print('Last NFT listed was number', START-1)
	f.close()
	quit()

url = 'https://opensea.io/collection/'+COLLECTION_NAME+'?search[query]='

# list all NFTS
for num in range(START, NUMBER_NFTs+1):
	try:
		# search for element num
		numWithZeros = str(num).zfill(4)
		urlWithQuery = url+numWithZeros
		driver.get(urlWithQuery)

		# go to sell link from card
		xpath='//*[@id="__next"]/div[1]/main/div/div/div[4]/div/div/div/div[3]/div[3]/div[2]/div/div/div/div/article/a'
		element = WebDriverWait(driver, TIME_FOR_PAGE_LOADS).until(lambda d: d.find_element(By.XPATH, xpath))
		link = element.get_attribute("href")
		sellLink = link+'/sell'
		driver.get(sellLink)

		# get NFT name
		xpath='//*[@id="__next"]/div[1]/main/div/div/div[1]/div[2]/div/a/div/div[2]/div/div[2]/span[2]'
		element = WebDriverWait(driver, TIME_FOR_PAGE_LOADS).until(lambda d: d.find_element(By.XPATH, xpath))
		nftName = element.text

		# click price box
		xpath='//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[2]/input'
		element = WebDriverWait(driver, TIME_FOR_PAGE_LOADS).until(lambda d: d.find_element(By.XPATH, xpath))

		# type price and click complete listing
		element.send_keys('.01')
		xpath='//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[5]/button'
		element = WebDriverWait(driver, TIME_FOR_PAGE_LOADS).until(lambda d: d.find_element(By.XPATH, xpath))
		element.click()

		# click sign button
		xpath='/html/body/div[4]/div/div/div/section/div/div/section/div/div/div/div/div/div/div/button'
		element = WebDriverWait(driver, TIME_FOR_PAGE_LOADS).until(lambda d: d.find_element(By.XPATH, xpath))
		element.click()

		# wait til user signs 
		xpath='/html/body/div[4]/div/div/div/div[1]/section/p/a'
		element = WebDriverWait(driver, TIME_FOR_USER_INTERACTIONS).until(lambda d: d.find_element(By.XPATH, xpath))

		print('Just listed '+nftName+'! See it here:', urlWithQuery)
	except:
		print('Last NFT listed was number', num-1)
		f.seek(0)
		f.write(str(num))
		f.truncate()
		f.close()
		quit()
