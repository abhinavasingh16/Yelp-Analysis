import json
import pandas as pd
import sys
import os

if __name__=="__main__":
	if len(sys.argv) > 3:
		file_name = 'yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_{0}.json'.format(sys.argv[1])
		data = []
		with open(file_name) as data_file:
			for line in data_file:
				data.append(json.loads(line))
		df = pd.DataFrame(data)
		#Define exploratory analysis
