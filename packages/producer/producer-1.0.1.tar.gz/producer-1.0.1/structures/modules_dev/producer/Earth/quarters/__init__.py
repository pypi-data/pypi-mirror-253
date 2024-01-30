

'''
	dreams:
		returns a stock trading day that's close to
		1/4 of the year.
		
			that way the closest stock trading day
			from the date that a financial document
			such as income statement, balance sheet,
			etc. can be determined,
			
				so that something like 2023-q1, 2023-q2
				for the document can be determined
'''

'''
	from producer.Earth.quarters import quarters

	quarter_places = quarters.learn ([ 2022, 2021, 2020 ])
	for year in quarter_places:
		for year_quarter in quarter_places [year]:	
			print (year, year_quarter)
'''

'''
	proceeds = quarters.learn ([ 2022, 2021, 2020 ], return_list = True)
	
	[
		[ 2022, 1, "2022-03-31" ]
	]
'''

'''	
	END_DATE = quarters.learn ({
		"year": 2023
		"QUARTER": 1
	})
'''


def learn (params, return_list = False):
	places = {
		"2023": {
			"4": "2024-01-02",
			"3": "2023-09-29",
			"2": "2023-06-30",
			"1": "2023-03-31"
		},
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
	}

	if (type (params) == list):
		if (return_list == False):
	
			proceeds = {}
			for year in params:
				year = str (year)
			
				proceeds [ year ] = places [ year ]
					
			return proceeds
			
		else:
			dates = []
			for year in params:
				year = str (year)
			
				for Q in places [ year ]:
					dates.append ([ year, Q, places [ year ][ Q ] ])
			
					
			return dates
	
	if (type (params) == dict):
		Q = str (params ["quarter"])
		Y = str (params ["year"])  	
	
		return places [ Y ] [ Q ]
		
	raise Exception ("The quarters params not recognized.", params)