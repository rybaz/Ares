from subprocess import Popen, PIPE

process = Popen(['grep python'], stdout=PIPE, stderr=PIPE)

stdout, stderr = process.communicate()