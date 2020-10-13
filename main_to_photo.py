def main_to_photo3(start_photo,photo_num,seed):
	try:
		by_xp('//*[@id="conts"]/div[1]/div/div[3]/div[1]/div[1]/button')
	except selenium.common.exceptions.ElementNotInteractableException:
		a=5
	except selenium.common.exceptions.NoSuchElementException:
		a=5

	if start_photo==1 and chinmil_on:
		by_xp('//*[@id="artistFacebook"]')
		close_tab()
		by_xp('//*[@id="artistTwitter"]')
		close_tab()
		print("did chinmil")
		by_xp('//*[@id="degreeType"]/a') # 친밀도

		delay=10
		err_count=0
		while True:
			try:    
				myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="afrFacebook"]')))
				by_xp('//*[@id="afrFacebook"]')
				close_tab()
				by_xp('//*[@id="afrTwitter"]')
				close_tab()
				by_xp('/html/body/div[2]/div/div/div/div/div[3]/button')
				err_count=0
				break
			except ElementNotVisibleException:
				print("Loading took too much time!")
			except selenium.common.exceptions.NoSuchElementException:
				print("Loading took too much time!")
			except selenium.common.exceptions.StaleElementReferenceException:		
				err_count+=1
				print('waiting')	
				if err_count==15:
					ml()
					return 1


	
	print("into the photo")

	err_count=0
	shut_down_count=0
	for i in range(start_photo,photo_num+1,1):
		global now_photo
		now_photo=i
		photo_url='https://www.melon.com/artist/photo.htm?artistId='+str(seed)+'#params%5BorderBy%5D=NEW&params%5BlistType%5D=1&params%5BartistId%5D='+str(seed)+'&po=pageObj&startIndex='
		photo_url+=str(now_photo)
		driver.get(photo_url)
		while True:
			try:
				by_xp('//*[@id="pageList"]/div/div/ul/li[1]/div/div/a/span[1]') # 첫 포토 들어오기
				break
			except selenium.common.exceptions.ElementNotInteractableException:
				a=3
			except selenium.common.exceptions.StaleElementReferenceException:
				a=3	

		print("photo now : ",i)
		while True:
			try:
				by_xp('//*[@id="photoFacebook"]')
				close_tab()
				
				by_xp('//*[@id="photoTwitter"]')
				close_tab()
				err_count=0
				shut_down_count=0
				break
			except ElementNotVisibleException:
				shut_down_count+=1
				print("Loading took too much time!")
				if shut_down_count==25:
					print("LOADING ERROR!")
					return 0
			except selenium.common.exceptions.NoSuchElementException:
				shut_down_count+=1
				print("Loading took too much time!")
				if shut_down_count==25:
					print("LOADING ERROR!")
					return 0
			except selenium.common.exceptions.StaleElementReferenceException:		
				shut_down_count+=1
				print("Loading took too much time!")
				if shut_down_count==25:
					print("LOADING ERROR!")
					return 0
			except selenium.common.exceptions.WebDriverException:
				err_count+=1
				print('waiting!!')	
				if err_count==15:
					ml()
					global was_error
					was_error=1
					return 1

	driver.back()	
	return 0
