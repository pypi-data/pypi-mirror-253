


'''
	python3 status.proc.py "Earth/quarters/status_quarters_3.py"
'''

import producer.Earth.quarters as quarters
import json

def check_1 ():
	date = quarters.learn ({
		"year": 2023,
		"quarter": 1
	})
		
	assert (date == "2023-03-31")
	
checks = {
	'check 1': check_1
}