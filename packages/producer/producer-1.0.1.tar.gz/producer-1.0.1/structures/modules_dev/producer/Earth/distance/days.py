

'''
	from producer.Earth.distance.days import learn_days_distance
	
	days_distance = learn_days_distance (
		date_1 = "2020-03-31",
		date_2 = "2020-03-30",
		format = "YYYY-MM-DD"
	)
'''

'''
	https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
		https://stackoverflow.com/questions/8142364/how-to-compare-two-dates
'''	

import datetime


def learn_days_distance (
	date_1 = "",
	date_2 = "",
	
	format = "YYYY-MM-DD"
):
	if (format == "YYYY-MM-DD"):
		split_1 = list (map (lambda D : int(D), date_1.split ("-")))
		split_2 = list (map (lambda D : int(D), date_2.split ("-")))

		D1 = datetime.datetime (split_1[0], split_1[1], split_1[2])
		D2 = datetime.datetime (split_2[0], split_2[1], split_2[2])

		change = D2 - D1;
				
		return change.days
		
	raise Exception (f'Format "{ format }" isn\'t a possibility.')
