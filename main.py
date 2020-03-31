#integrating scraper and crawler and making tool zoldyck
import os

os.system("tput setaf 1")
os.system("color 1b")
print("\t\t\t\t\t\t\tZOLDYCK")
os.system("tput setaf 5")
print("\t\t\t\t\t\t\t_______")
while True:
	print("""\t\t\tpress 1: To crawl a website
\t\t\tpress 2: To scrap data from the crawled websites
\t\t\tpress 3: To insert data into the database 
\t\t\tpress 4: Exit""")

	x = input("ZOLDYCK>")

	if int(x) == 1:
		print("Give the website URL")
		website = input("ZOLDYCK>")
		file = open('website_link.txt','w')
		file.write(website)
		file.close()
		#os.system("py crawl.py")
		os.system("python3 crawl.py")
		

	elif int(x) == 2:
		#os.system("py scrap.py")
		os.system("python3 scrap.py")
	elif int(x) == 4:
		exit()
