# Author: John Landehol [TA]

class syntax_error(Exception):
    """ Usage:
        raise syntax_error(message, queue)

        Example:
        raise syntax_error('Saknad stor bokstav', q)
    """
    def __init__(self, message, rest_of_q = None):
        self.message = message
        if rest_of_q:
            """ Excepts rest_of_q to be an iterable
                If custom class: you need to add __iter__ and __next__ methods to it.
            """
            self.stack_trace = "".join(rest_of_q)
            """
            self.stack_trace = ""
            while not rest_of_q.empty:
                self.stack_trace += rest_of_q.pop()
            """
        else:
            self.stack_trace = rest_of_q

    def __str__(self):
        return f'{self.message} vid radslutet {self.stack_trace}'.strip()

    def __repr__(self):
        return self.__str__()