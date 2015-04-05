import gras
import numpy
from gnuradio import gr
from gnuradio import blocks

from Queue import Queue

class BufferBlock(gras.Block):
    def __init__(self, buffer_limit = 10):
        gras.Block.__init__(self,
            name    = "csim",
            in_sig  = [numpy.float32],
            out_sig = [numpy.float32])

        self.queue  = Queue(maxsize=buffer_limit)

    def work(self, input_items, output_items):
        '''
        Work Function
        '''

        if self.queue.full():
            print "Throw Exception"
        else:
            if not self.queue.empty():
                out = self.queue.get()

            self.queue.put(input_items[0])

        self.consume(0, len(input_items[0]))
        self.produce(0, len(out))
