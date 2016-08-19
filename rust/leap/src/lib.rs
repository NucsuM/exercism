//use std::ops::Rem;

pub fn is_leap_year(year:i32) -> bool {
	if (year % 4 == 0) {
		if ((year % 100 != 0) || (year % 400 == 0)){
			return true;
			}
            
		}
		return false;
	}
	
	
/* python
def is_leap_year(year):
    if (year % 4 == 0):
        if ((year % 100 != 0) or (year % 400 == 0)):
            return True
    return False
*/