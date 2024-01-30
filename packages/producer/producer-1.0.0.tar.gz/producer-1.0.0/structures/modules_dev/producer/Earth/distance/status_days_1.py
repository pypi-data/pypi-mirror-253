



from producer.Earth.distance.days import learn_days_distance
	

def check_1 ():
	days_distance = learn_days_distance (
		date_1 = "2020-03-31",
		date_2 = "2020-03-30"
	)
	
	assert (days_distance == -1)
	
	
def check_2 ():
	days_distance = learn_days_distance (
		date_1 = "2020-03-31",
		date_2 = "2028-03-30"
	)
	
	assert (days_distance == 2921)
	
	
checks = {
	"check 1": check_1,
	"check 2": check_2
}