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
				line = psm.read_serial()
				if (line != ''):

					#TODO

					print('')

			except:
				print('Problema na comunicacao com o Arduino! :(')
				time.sleep(1)
				psm.ini()

#Inicia os Threads e seta as funcoes de tratamento
#Thread que verifica se o gravador esta conectado
t1 = threading.Thread(target=serialCheck)
#Thread que trata a porta serial
t2 = threading.Thread(target=monitorSerial)
#inicia
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
