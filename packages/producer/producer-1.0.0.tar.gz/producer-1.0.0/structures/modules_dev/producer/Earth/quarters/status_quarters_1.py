


'''
	python3 status.proc.py "Earth/quarters/status_quarters_1.py"
'''

import json
import producer.Earth.quarters as quarters

def test_1 ():
	years = quarters.learn ([ 2022, 2021, 2020 ])
	for year in years:
		for quarter in years [year]:	
			print (year, quarter)
	
	
	print (json.dumps (years, indent = 2))
	
	assert (
		json.dumps ({
			"2022": {
				"4": "2023-01-03",
				"3": "2022-09-30",
				"2": "2022-06-30",
				"1": "2022-03-31"
			},
			"2021": {
				"4": "2022-01-03",
				"3": "2021-09-30",
				"2": "2021-06-30",
				"1": "2021-03-31"
			},
			"2020": {
				"4": "2021-01-04",
				"3": "2020-09-30",
				"2": "2020-06-30",
				"1": "2020-03-31"
			}
		}, indent = 2) ==
		
		json.dumps (END_DATES, indent = 2)
	)
	


	return;