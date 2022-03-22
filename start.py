from input_module import take_input
from process_module import process
from output_module import output

while(True):
    #take input
    i = take_input()

    #process input
    o = process(i)

    #output
    output(o)