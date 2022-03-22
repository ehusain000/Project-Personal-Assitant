from output_module import output
from time_module import get_time


def process(query):

    if "what is the time" in query:
        return ("the time is " + get_time())
    else:
        return "nothing to return"