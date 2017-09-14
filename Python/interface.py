from PythonSerialMonitor import *
import threading
import time
import sys

psm = PythonSerialMonitor()
psm.ini()

finish = psm.getEnd()

def serialCheck():
	while not finish:
		while not psm.get_status():
			time.sleep(1)
			psm.ini()
			if finish:
				break

def monitorSerial():
	while not finish:
		if psm.get_status():
			try:
				_line = psm.read_serial()
				if (_line != ''):

					#TODO

					print('')

			except:
				print('Problema na comunicacao com o Arduino! :(')
				time.sleep(1)
				psm.ini()

t1 = threading.Thread(target=serialCheck)
t2 = threading.Thread(target=monitorSerial)

t1.start()
t2.start()
while(True):
	if finish:
		t1.join()
		t2.join()
		psm.close()
		sys.exit(1)
		break
	finish = psm.getEnd()
