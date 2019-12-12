import wget
from random import sample
import os
import sys

s3_root_path = "s3://dataforgood-fb-data/csv/month=2019-06/country=WLF/type=men/WLF_men.csv.gz"
out_path = "_data"

if __name__ == "__main__":

	wget.download(s3_root_path, out_path)

	# try:
	# 	num_pages = sys.argv[1]
	# except:
	# 	num_pages = 50
	# downloadCrawlData(num_pages)

