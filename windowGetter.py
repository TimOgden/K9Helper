from win32gui import GetWindowText, GetForegroundWindow
import time
import datetime
from faceDetector import hasFace, detect, close
check_freq_sec = 30
applications_time = {}
num_hours = 12
t_end = time.time() + num_hours * 60 * 60
start_time = 0
end_time = 0
def main():
	start_time = datetime.datetime.now()
	while time.time() < t_end:
		if hasFace():
			log_window()
			print('.')
			print(window())
		else:
			print('No face found')
		time.sleep(check_freq_sec)
	end_time = datetime.datetime.now()
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
		val += start_time + '\n'
		for key in applications_time:
			val += key + "\n" + str(applications_time[key]) + "\n"
		val += end_time + '\n'
		f.write(val)

def window():
	return GetWindowText(GetForegroundWindow())

main()