import datetime
print("××××× Welcome to 'Your exact age calculator' ×××××\n")
print("Follow the instructions to get your age!\n")
#Inputs
usr_name = input("Tell me your name so that I can remember you: ")
while True:
	print(usr_name,"when were you born (dd/mm/yyyy): ",end ="")
	dob = input()
	if len(dob) != 10 or dob[2] != '/' or dob[5] != '/':
		print("Invalid Date, Try Again...")
		continue
	elif len(dob) == 10 and dob[2] == "/" and dob[5] == '/':
		while True:
			day,month,year = dob.split('/')
			isValidDate = True
			try :
				datetime.datetime(int(year),int(month),int(day))
			except ValueError :
				isValidDate = False
			if isValidDate == False:
				print ("Input date is not valid...")
				continue
			elif isValidDate == True:
				break
		break
				
#Calculator
birth_date = datetime.datetime.strptime(dob,"%d/%m/%Y")
current_date = datetime.datetime.now()
date_diff = current_date - birth_date

age_years = (date_diff.total_seconds()) / (365.242 * 24 * 3600)

age_months = age_years * 12 - int(age_years) * 12

age_days = age_months * (365.242 / 12) - int(age_months) * (365.242 / 12)

age_hours = age_days * 24 - int(age_days) * 24

age_minutes = age_hours * 60 - int(age_hours) * 60

age_seconds = age_minutes * 60 - int(age_minutes) * 60

print("")
print(usr_name,"you are",int(age_years),"years,",int(age_months),"months,",int(age_days),"days,",int(age_hours),"hours,",int(age_minutes),"minutes and",int(age_seconds),"seconds old!\n")

print("Total Years:    ",int(age_years))
print("Total Months:   ",int(age_years * 12))
print("Total Days:     ",int(age_years * 365.242))
print("Total Hours:    ",int(age_years * 365 * 24))
print("Total Minutes:  ",int(age_years * 365 * 24 * 60))
print("Total Seconds:  ",int(age_years * 365 * 24 * 60 * 60))
print("")
print("Thanks for using this calculator, hope you liked it. Please consider rating it...\n")
rating = None
while rating is None:
		rate_value = input("What would you rate this program(?/5): ")
		try:
			rating = int(rate_value)
		except ValueError:
			print("Invalid Rating, Try again...")
if rating >= 5:
	print("Looks like you are highly satisfied with this program :D")
elif rating == 4 or rating == 3:
	print("Ohh! Next time I'll try my best to change this '",rating,"' into 5 ;D")
elif rating == 1 or rating == 2:
	print("I am sorry if I wasn't good, I'll try my best next time :\\")
elif rating < 1:
	print("Ohh! I am really sorry for your bad experience with me :(")