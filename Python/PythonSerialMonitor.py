import sys
import threading
import time
import Queue
import serial

class PythonSerialMonitor():
    def __init__(self):
        self.windows = False
        self.unix = False
        self.fd = None
        self.old_settings = None

        try:
            # Windows
            import msvcrt
            self.windows = True
        except ImportError:
            # Unix
            import sys, tty, termios
            self.fd = sys.stdin.fileno()
            self.old_settings = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)
            self.unix = True

        self.input_queue = Queue.Queue()
        self.stop_queue = Queue.Queue()
        self.pause_queue = Queue.Queue()

        self.input_thread = threading.Thread(target=self.add_input, args=(self.input_queue,self.stop_queue,self.pause_queue,))
        self.input_thread.daemon = True
        self.input_thread.start()

        self._end = False

    def getch(self):
        if self.unix:
            import sys, tty, termios
            try:
                tty.setcbreak(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)
            return ch
        if self.windows:
            import msvcrt
            return msvcrt.getch()

    def cleanUp(self):
        if self.unix:
            import sys, tty, termios
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

    def add_input(self, input_queue, stop_queue, pause_queue):
        while True:
            input_queue.put(self.getch())
            if not pause_queue.empty():
                if pause_queue.get() == 'pause':
                    while True:
                        if not pause_queue.empty():
                            if pause_queue.get() == 'resume':
                                break
            if not stop_queue.empty():
                if stop_queue.get() == 'stop':
                    break

    def ini(self):
        baud = 9600
        baseports = ['/dev/ttyUSB', '/dev/ttyACM', 'COM', '/dev/cu.usbmodem142']
        self.ser = None

        for baseport in baseports:
            if self.ser:
                break
            for i in xrange(0, 64):
                try:
                    port = baseport + str(i)
                    self.ser = serial.Serial(port, baud, timeout=1)
                    print("Monitor: Opened " + port + '\r')
                    break
                except:
                    self.ser = None
                    pass

        if not self.ser:
            print("Monitor: O Arduino nao esta conectado! :(")
            print("Monitor: Qualquer tecla para tentar novamente ou segurar \'esc\' para sair.")
            while True:
                print self.input_queue.get()
                if not self.input_queue.empty():
                    keyboardInput = self.input_queue.get()

                    if ord(keyboardInput) == 27:
                        self.stop_queue.put('stop')
                        self.cleanUp()
                        self._end = True
                        sys.exit(1)
                        break
                    else:
                        # Pressing any key other than 'esc' will continue the monitor
                        break
                break
        #self.ser.ini()
    def getEnd(self):
        return self._end;
    def get_status(self):
        if self.ser:
            return True
        else:
            return False

    def read_serial(self):
        return self.ser.readline()
    def get_serial(self):
        return self.ser
    def write_serial(self, msg):
        self.ser.write(msg)
    def close(self):
        print 'Serial Close.'
        self.stop_queue.put('stop')
        self.cleanUp()
        sys.exit(1)
    def run(self):
        msg_serial = ''
        while True:
            if not self.input_queue.empty():
                keyboardInput = self.input_queue.get()
                msg_serial = msg_serial + keyboardInput
                print("Keyboard: " + msg_serial)
                if ord(keyboardInput) == 10:
                    print ('Mensagem enviada!')
                    self.ser.write(msg_serial)
                    msg_serial =''
                if ord(keyboardInput) == 27:
                    self.stop_queue.put('stop')
                    self.cleanUp()
                    sys.exit(1)
            # Check for Teensy output:
            try:
                bytesToRead = self.ser.inWaiting() # get the amount of bytes available at the input queue
                if bytesToRead:
                    line = self.ser.read(50) # read the bytes
                    print("Teensy: " + line.strip())
            except IOError:
                # Manually raise the error again so it can be caught outside of this method
                raise IOError()