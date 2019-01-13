from win32gui import GetWindowText, GetForegroundWindow
import time
import datetime
from faceDetector import hasFace, detect, close
check_freq_sec = 10
applications_time = {}
num_hours = 0.08333333333 # 5 mins
t_end = time.time() + num_hours * 60 * 60

def main():
	while time.time() < t_end:
		if hasFace():
			log_window()
			print('.')
			print(window())
		else:
			print('No face found')
		time.sleep(check_freq_sec)
	publish_log()
	close()
	print('done')


def log_window():
	w = window()
	if w in applications_time:
		applications_time[w] += check_freq_sec/60
	else:
		applications_time[w] = check_freq_sec/60

def publish_log():
	now = datetime.datetime.now()
	with open('windowslog-{}-{}-{}.txt'.format(now.month,now.day,now.year), 'w') as f:
		val = ""
		for key in applications_time:
			val += key + "\n" + str(applications_time[key]) + "\n"
		f.write(val)

def window():
	return GetWindowText(GetForegroundWindow())

main()