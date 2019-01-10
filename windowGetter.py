from win32gui import GetWindowText, GetForegroundWindow
import time

check_freq_sec = 30
applications_time = {}
num_minutes = 60*24
t_end = time.time() + num_minutes * 60

def main():
	while time.time() < t_end:
		log_window()
		print('.')
		time.sleep(check_freq_sec)
	publish_log()
	print('done')


def log_window():
	w = window()
	if w in applications_time:
		applications_time[w] += check_freq_sec/60
	else:
		applications_time[w] = check_freq_sec/60

def publish_log():
	with open('windowslog.txt', 'w') as f:
		val = ""
		for key in applications_time:
			val += key + "||||" + str(applications_time[key]) + ",\n"
		f.write(val)

def window():
	return GetWindowText(GetForegroundWindow())

main()