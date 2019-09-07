# Prob6 but all in one line
[print(f"{y} is the year of the {['snake','horse','sheep','monkey','rooster','dog','pig','rat','ox','tiger','rabbit','dragon'][(int(y)-1965)%12]}") for y in [input() for t in range(int(input()))]]
