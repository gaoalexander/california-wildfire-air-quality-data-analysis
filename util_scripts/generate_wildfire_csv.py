import json
import csv
import urllib.request

def parsePage_WriteToCSV(request, wildfire_data_csv_path, doc_num):
	html = urllib.request.urlopen(request).read().decode('ascii', 'ignore')
	after_this = "InitialData = "
	before_this = "}];"
	for i in range(len(html)):
		if html[i : i + 14] == after_this:
			start_index = i + 14
		if html[i : i + 3] == before_this:
			end_index = i + 1
			break
	fire_dict = json.loads(html[start_index : end_index + 1])
	csvwriter = csv.writer(open(wildfire_data_csv_path, 'a'))
	for i, each in enumerate(fire_dict):
		if i == 0 and doc_num == 0: csvwriter.writerow(each.keys())
		csvwriter.writerow(each.values())

def createWildfireCSV(wildfire_data_csv_path, fire_ca_url):
	doc_num = 0
	for year in range(2013, 2020):
		print("Processing Year: ", year)
		url = fire_ca_url + str(year) + "/"
		parsePage_WriteToCSV(url, wildfire_data_csv_path, doc_num)
		doc_num += 1

if __name__ == "__main__":
	wildfire_data_csv_path = "/Users/GAO/Documents/NYUClasses_Fall2019/FoundationOfDataScience/Project/data/wildfire_data.csv"
	fire_ca_url = "https://www.fire.ca.gov/incidents/"
	createWildfireCSV(wildfire_data_csv_path, fire_ca_url)