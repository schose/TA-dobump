from __future__ import absolute_import, division, print_function, unicode_literals
import app

from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
import sys
import time
from six.moves import range


@Configuration()
class GenerateHelloCommand(GeneratingCommand):

    count = Option(require=True, validate=validators.Integer(0))

    def generate(self):
        for i in range(1, self.count + 1):
            text = 'Hello World %d' % i
            yield {'_time': time.time(), 'event_no': i, '_raw': text}

dispatch(GenerateHelloCommand, sys.argv, sys.stdin, sys.stdout, __name__)