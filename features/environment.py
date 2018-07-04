from selenium import webdriver

def before_all(context):
	chromedriver = 'features/chromedriver'
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	context.browser = webdriver.Chrome(executable_path=chromedriver,chrome_options=options)
	#self.browser = webdriver.Chrome('features/chromedriver')
	context.browser.maximize_window()
	context.browser.implicitly_wait(5)

def after_all(context):
    context.browser.quit()
