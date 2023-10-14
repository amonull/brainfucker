
from .exceptions import No_loop_end, Cant_reach_pointer

class BrainfuckInterpeter:
    def __init__(self, brainfuck_string: str, reference_to_cells: list[int], break_points: list[int]) -> None:
        # brainfuck vars
        self.brainfuck_string = brainfuck_string
        self.brainfuck_string_pos = 0
        self.cells = reference_to_cells
        self.pointer = 0

        # debugger vars
        self.pause = False
        self.break_points = break_points


    def increment_pointer_value(self):
        """
        increments value inside pointer by 1
        loops to 0 if value is 255
        """
        # self.cells[self.pointer] = 0 if self.cells[self.pointer] == 255 else self.cells[self.pointer] + 1
        self.cells[self.pointer] = (self.cells[self.pointer] + 1) % 256


    def decrement_pointer_value(self):
        """
        decrements value inside pointer by 1
        loops to 255 is value is 0
        """
        # self.cells[self.pointer] = 255 if self.cells[self.pointer] == 0 else self.cells[self.pointer] + 1
        self.cells[self.pointer] = (self.cells[self.pointer] - 1) % 256


    def increment_pointer(self):
        """
        moves to next pointer
        """
        self.pointer += 1
        if len(self.cells) < self.pointer:
            self.cells.append(0) # make new cell


    def decrement_pointer(self):
        """
        moves to previous pointer
        """
        self.pointer -= 1
        if self.pointer == 0:
            raise Cant_reach_pointer


    def print_char(self):
        """
        prints ascii value of current pointer
        """
        print(chr(self.cells[self.pointer]))


    def get_char(self):
        """
        gets single char from user and puts to current pointer
        """
        self.cells[self.pointer] = ord(input()[0])


    def loop_start(self):
        """
        starts loop using value inside pointer as range

        sets self.brainfuck_string_pos to end of loop
        """
        try:
            # nested loops shouldn't be a problem since they wont be execed again after this function
            old_brainfuck_string_pos = self.brainfuck_string_pos
            self.brainfuck_string_pos = self.brainfuck_string.find("]", self.brainfuck_string_pos)+1 # jump to end of loop
            char_range_to_exec = (old_brainfuck_string_pos+1, self.brainfuck_string_pos-2)
        except ValueError:
            raise No_loop_end

        for _ in range(0, self.cells[self.pointer]):
            for i in range(char_range_to_exec[0], char_range_to_exec[1]):
                self.check_char(self.brainfuck_string[i])

    
    def check_char(self, char: str):
        """
        matches chars and executes correct functions
        """
        if char == "+":
            self.increment_pointer_value()
        elif char == "-":
            self.decrement_pointer_value()
        elif char == ">":
            self.increment_pointer()
        elif char == "<":
            self.decrement_pointer()
        elif char == ".":
            self.print_char()
        elif char == ",":
            self.get_char()
        elif char == "[":
            self.loop_start()
        # ] matched in loop_start
        # no need for else everything else treated as comments


    def run(self):
        """
        runner code reading self.brainfuck_string char by char
        """
        while len(self.brainfuck_string) > self.brainfuck_string_pos:
            self.check_char(self.brainfuck_string[self.brainfuck_string_pos])
