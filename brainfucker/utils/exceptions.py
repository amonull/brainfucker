class No_loop_end(Exception):
    "No ] found after [" # ] added to fix indentation on my ide
    pass

class Cant_reach_pointer(Exception):
    "cannot go to cell less than cell #0"
