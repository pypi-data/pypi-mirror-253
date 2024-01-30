
'''
	import producer.Earth.current as current
	the_current = current.learn ()
'''

from datetime import datetime

def learn (
	format = "YYYY-MM-DD"
):
	now = datetime.now ()

	if (format == "YYYY-MM-DD"):
		month = str (now.month);
		if (len (month) == 1):
			month = "0" + month
			
		day = str (now.day)
		if (len (day) == 1):
			day = "0" + day
	
		return str (now.year) + "-" + month + "-" + day

	return now;