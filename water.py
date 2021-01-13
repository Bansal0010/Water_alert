import time

from plyer import notification

if __name__ == '__main__':
 	notification.notify(
 		title = "**Please Drink Water Now!!",
 		message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
 	 app_icon = "path to your .ico file",
 		timeout= 5
 		)
 		#	time.sleep(6)
 			# time.sleep(60*60)
