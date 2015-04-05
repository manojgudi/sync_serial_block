#!/usr/bin/python

import gras
import numpy
import serial
import threading

class ser(gras.Block):
    '''
    Serial Block
    '''

    def __init__(self, pipe_name, port, baud, bytesize, parity, stopbits):
        gras.Block.__init__(self,
            name="ser",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

        try:
            self.ser_obj = serial.Serial(port, baud,  bytesize, parity,  stopbits)
            self.ser_obj.open()
            print("serial found on " + port )
        except:
            print "Couldn't Open Serial Port " + port + " Failed"

        # Pipe names                                                               |    def __init__(self, pipe_name, port, baud, bytesize, parity, stopbits):         
        self.pipe_name = pipe_name                                                 |        gras.Block.__init__(self,                                                  
                                                                                   |            name="ser",
        # Pipe templates                                                           |            in_sig=[numpy.float32],
        self.pipe_template = pipes.Template()                                      |            out_sig=[numpy.float32])
        self.pipe_template.append('tr a-z A-Z', '--')

        self.n = 1

    def acceptData(self,):
        '''
        Ready to get data from buffer block
        '''
        pipe_file = pt.open(self.pipe_name, 'w')
        pipe_file.write(str(time.time()))
        pipe_file.close()


    def work(self, input_items, output_items):
        '''
         work function
        '''
        self.n = input_items[0][0]
        out = output_items[0][:self.n]
        # Input is size of output_items to be returned

        for i in range(self.n):
            # Try catch block to avoid Error
            # ValueError: invalid literal for int() with base 10: '\xfe354\r\n'
            try:
                out[i] = int(self.ser_obj.readline())
            except:
                pass

        print "OUT", out[:self.n]
        self.acceptData()

        self.produce(0,len(out)) # Produce from port 0 output_items
        self.consume(0,1) # Consume from port 0 input_items

