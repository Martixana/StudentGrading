def compute_grade():
	try:
	    score = raw_input("What was the student's score, between 0.0  - 1.1? ")
	    s = float(score)
	    if s >= 0.9 and s <= 1.1:
		    grade = 'A'
	    elif s >= 0.8 and s < 0.9:
		    grade = 'B'
	    elif s >= 0.7 and s < 0.8:
		    grade = 'C'
	    elif s >= 0.6 and s < 0.7:
		    grade = 'D'
	    elif s <= 0.6:
		    grade = 'F'
	    return grade
	except: 
		print "Bad score. Please try again with a score between 0.1-1.0"
	
	
print "You final grade is: " + compute_grade()