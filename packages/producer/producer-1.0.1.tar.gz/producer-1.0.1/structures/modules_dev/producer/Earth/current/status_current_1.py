

import producer.Earth.current as current


def check_1 ():
	the_current = current.learn ()
	
	the_split = the_current.split ("-")

	assert (len (the_split [1]) == 2)
	assert (len (the_split [2]) == 2)

	assert (int (the_split [1]) >= 1 and int (the_split [1]) <= 12)
	assert (int (the_split [2]) >= 1 and int (the_split [2]) <= 31)

checks = {
	"check 1": check_1	
}