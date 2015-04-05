import gras
import numpy

from gnuradio import gr
from gnuradio import blocks

from Queue import Queue
from time  import time

class BufferBlock(gras.Block):
    def __init__(self, buffer_limit = 10, pipe_name):
        '''
        set buffer_limit = 0 to have infinite buffer
        '''
        gras.Block.__init__(self,
            name       = "csim",
            in_sig     = [numpy.float32],
            out_sig    = [numpy.float32])

        self.queue     = Queue(maxsize = buffer_limit)

        # Epoch value
        self.last_evnt = time()

        # Pipe names
        self.pipe_name = pipe_name

        # Pipe templates
        self.pipe_template = pipes.Template()
        self.pipe_template.append('tr a-z A-Z', '--')

    def isReady(self,):
        '''
        Checks if a block further is ready to receive data
        '''

        pipe_value = float(open(self.pipe_name).read())

        if pipe_value - self.last_evnt > 0:
            return (True, pipe_value)
        else:
            return (False, pipe_value)

    def work(self, input_items, output_items):
        '''
        Work Function
        '''

        if self.queue.full():
            print "Buffer Full Throw Exception"
        else:
           self.queue.put(input_items[0])

        self.consume(0, len(input_items[0]))

        shoud_send, self.last_evnt = self.isReady()

        # Assuming this triggers output
        if should_send:
            if not self.queue.empty():
                out = self.queue.get()
            # Send None for first time
            else:
                out = None

            self.produce(0, len(out))
