
universities =	[
	['Caltech', 2175, 37704],
	['Harvard', 19627, 39849],
	['MIT', 10566, 40732],
	['Princeton', 7802, 37000],
	['Rice', 5879, 35551],
	['Stanford', 19535, 40569],
	['Yale', 11701, 40500]
]



def enrollment_stats(universities):
	enrollment = []
	tuition = []

	for i in universities:
		enrollment.append(i[1])
		tuition.append(i[2])
	return enrollment, tuition


def mean(blah):
	msum = 0
	for i in blah:
		msum += (msum+i)
	return int(msum) / len(blah)

def median(blah):
	bsort = sorted(blah)
	length = len(bsort)
	if length % 2 == 1:
		return bsort[length//2]
	else:
		return sum(bsort[length//2-1:length//2+1])/2.0
	
totals = enrollment_stats(universities)


print("*****" * 5)
print("Total students:   {}".format(sum(totals[0])))
print("Total tuition:  $ {}".format(sum(totals[1])))
print("\nStudent mean:     {}".format(mean(totals[0])))
print("Student median:   {}".format(median(totals[0])))
print("\nTuition mean:   $ {}".format(mean(totals[1])))
print("Tuition median: $ {}".format(median(totals[1])))
print("*****" * 5)