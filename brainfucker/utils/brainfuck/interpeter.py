#!/usr/bin/env python

from typing import Union, Callable

from ..exceptions import InterpeterExceptions

class Buffer:
    """
    class to handle everything to do with buffers
    like incrementig the current pointer or to change the current pointer
    """
    def __init__(self, cell_size: int, ptr_size: int) -> None:
        self.cells = [ptr_size] * cell_size
        self.pointer = 0
        self.exception_raiser = InterpeterExceptions()

    def inc_ptr_val(self) -> None:
        """
        increments value inside pointer by 1
        loops to 0 if value is 255
        """
        self.cells[self.pointer] = (self.cells[self.pointer] + 1) % 256

    def dec_ptr_val(self) -> None:
        """
        decrements value inside pointer by 1
        loops to 255 is value is 0
        """
        self.cells[self.pointer] = (self.cells[self.pointer] - 1) % 256

    def inc_ptr(self) -> None:
        """
        moves to next pointer
        """
        if self.pointer == len(self.cells):
            self.exception_raiser.CantIncrementPointer()
        else:
            self.pointer += 1

    def dec_ptr(self) -> None:
        """
        moves to previous pointer
        """
        if self.pointer == 0:
            self.exception_raiser.CantDecrementPointer()
        else:
            self.pointer -= 1

    def print_ptr(self) -> None:
        """
        prints ascii value of current pointer
        """
        print(chr(self.cells[self.pointer]), end="")

    def read_input(self) -> None:
        """
        gets single char from user and puts to current pointer
        """
        self.cells[self.pointer] = ord(input()[0])

    def __str__(self) -> str:
        return f"pointer: {self.pointer} value: {self.cells[self.pointer]} total cells: {len(self.cells)}"


class Interpeter(Buffer):
    def __init__(self,
                 brainfuck_string: str,
                 cell_size: int = 30000,
                 ptr_size: int = 0,
                 breakpoints: list[int] = []) -> None:
        # Buffer settings
        super().__init__(cell_size, ptr_size)

        # brainfuck settings
        self.brainfuck_string = brainfuck_string
        self.string_pos: int = 0
        self.jump_map: dict[int, int] = self._find_jumps()

        # debugger settings
        self.pause: bool = False
        self.breakpoints: list[int] = breakpoints

    def _find_jumps(self) -> dict[int, int]:
        """
        finds jumps inside the string and gets the equivalent positon to jump forward/backward
        """
        stack = []
        return_dict = {}
        
        while not self.string_pos == len(self.brainfuck_string):
            opchar = self.brainfuck_string[self.string_pos]
            if opchar == "[":
                stack.append(self.string_pos)
            elif opchar == "]":
                try:
                    r_bracket = stack.pop() # keep track of the last added r_bracket
                except IndexError:
                    self.exception_raiser.BraceMismatch()
                return_dict[r_bracket] = self.string_pos
                return_dict[self.string_pos] = r_bracket
                # keeping values as {r_bracket1: l_bracket1, l_bracket1: r_bracket1}

            self.advance()

        if stack:
            self.exception_raiser.BraceMismatch()

        self.string_pos = 0 # reset to 0

        return return_dict

    def _jump_foward(self):
        """
        if current pointer is 0 jump forward
        """
        if self.cells[self.pointer] == 0:
            self.string_pos = self.jump_map[self.string_pos]

    def _jump_backward(self):
        """
        if current pointer is not 0 jump backwards
        """
        if not self.cells[self.pointer] == 0:
            self.string_pos = self.jump_map[self.string_pos]

    def opchar_handler(self, opchar: str) -> Union[Callable[[], None], None]:
        """
        returns correct function depending on opchar
        """
        op_dict = { '+': self.inc_ptr_val,
                    '-': self.dec_ptr_val,
                    '>': self.inc_ptr,
                    '<': self.dec_ptr,
                    '.': self.print_ptr,
                    ',': self.read_input,
                    '[': self._jump_foward,
                    ']': self._jump_backward,
                    }
        return op_dict.get(opchar)

    def advance(self) -> None:
        """
        moves string position by 1
        """
        self.string_pos += 1
    
    def run(self) -> None:
        """
        start point
        reads brainfuck_string char by char
        """
        while not self.string_pos == len(self.brainfuck_string):
            opchar = self.brainfuck_string[self.string_pos]
            op_function = self.opchar_handler(opchar)
            if op_function:
                op_function()

            self.advance()
