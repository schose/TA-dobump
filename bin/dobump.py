from __future__ import absolute_import, division, print_function, unicode_literals

from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
import sys
import time
import os
from splunk.rest import simpleRequest

@Configuration()
class GenerateTextCommand(GeneratingCommand):

    def generate(self):
        fname = os.path.join(os.environ["SPLUNK_HOME"],  "var", "run", "splunk", "push-version.txt")
        with open(fname, 'r') as f:
            content = f.read()

        myversion = int(content)
        newversion = myversion+1
        with open(fname,"w") as f:
            f.write(str(newversion))

        sessionkey = self.service.token

        response, content = simpleRequest('/server/control/restart_webui', sessionKey = sessionkey, method='POST', raiseAllErrors=True)

        text = 'increased to version %s response: %s' % (newversion,response)
        yield {'_time': time.time(), 'event_no': '0', '_raw': text}

dispatch(GenerateTextCommand, sys.argv, sys.stdin, sys.stdout, __name__)