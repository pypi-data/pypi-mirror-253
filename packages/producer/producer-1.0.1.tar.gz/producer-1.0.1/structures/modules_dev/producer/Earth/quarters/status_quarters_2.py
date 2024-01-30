


'''
	python3 status.proc.py "Earth/quarters/status_quarters_2.py"
'''

import producer.Earth.quarters as quarters
import json

def check_1 ():
	dates = quarters.learn ([ 2022, 2021, 2020 ], return_list = True)

	assert (
		json.dumps (dates, indent = 4),
		json.dumps ([
			[
				"2022",
				"4",
				"2023-01-03"
			],
			[
				"2022",
				"3",
				"2022-09-30"
			],
			[
				"2022",
				"2",
				"2022-06-30"
			],
			[
				"2022",
				"1",
				"2022-03-31"
			],
			[
				"2021",
				"4",
				"2022-01-03"
			],
			[
				"2021",
				"3",
				"2021-09-30"
			],
			[
				"2021",
				"2",
				"2021-06-30"
			],
			[
				"2021",
				"1",
				"2021-03-31"
			],
			[
				"2020",
				"4",
				"2021-01-03"
			],
			[
				"2020",
				"3",
				"2020-09-30"
			],
			[
				"2020",
				"2",
				"2020-06-30"
			],
			[
				"2020",
				"1",
				"2020-03-31"
			]
		], indent = 4)
	)
		

checks = {
	'check 1': check_1
}