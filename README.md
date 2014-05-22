### Example
```
from ulogstash.inputs import file
from ulogstash.patterns import SYSLOG_RE, SUDO_RE
from multiprocessing import Process
from flumelogger.handler import FlumeHandler
import logging

fh = FlumeHandler(type='og')
logger = logging.getLogger("uLogstash")
logger.addHandler(fh)

def sudo_log(filename):
    input = file.File()
    loglines = input.follow(filename)
    for line in loglines:
        event = input.match_line(SYSLOG_RE, line)
        if event:
            sudo = input.match_line(SUDO_RE, event['message'].strip())
            if sudo:
                sudo['application'] = 'sudo'
                sudo['host'] = event['host']
                print sudo
                #logger.info(sudo)

def my_multiline_log(filename):
    input = file.File()
    loglines = input.follow(filename)
    for line in loglines:
        event = input.match_multiline(SYSLOG_RE, line)
        if event:
            print event
            #logger.info(event)

if __name__ == '__main__':
    Process(target=sudo_log, args=('./test-1.log',)).start()
    Process(target=my_multiline_log, args=('./test-2.log',)).start()
```
