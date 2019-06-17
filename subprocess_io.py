# python 通过subprocess通信
import subprocess
class Shell(object):
    def runCmd(self, cmd):
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate()
        return res.returncode, sout, serr, res.pid

shell = Shell()
while 1:
    input = raw_input('>')
    if input == 'exit' or input == 'bye' or input == 'end':
        break
    else:
        result = shell.runCmd(input)
    print "返回码：", result[0]
    print "标准输出：", result[1]
    print "标准错误：", result[2]