"""
Lexer
A lexer (generates tokens from a string input)
"""

from typing import Optional
import re
from txp_token import *

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        # debug info 
        self.line = 0
        self.column = 0
    
    def advanceChar(self) -> Optional[str]:
        """
        Advance lexer position and return next char, or None if EOF reached
        """
        try:
            result = self.source[self.position + 1]
            self.position += 1
            if result == '\n': 
                self.line += 1
                self.column = 0
            return result
        except IndexError:
            return None


    def peekChar(self) -> Optional[str]:
        """
        Peek 1 character ahead, but do not move lexer position
        Returns None if EOF reached
        """
        try:
            return self.source[self.position + 1]
        except IndexError:
            return None

    
    def lexToken(self) -> Token:
        """
        Lex next token and advance the lexer
        General entry point for handling lexing
        """ 
        char = self.advanceChar()
        if char == '<':
            return LBracket(self.line, self.column)
        elif char == '>':
            return RBracket(self.line, self.column)
        elif char == None:
            return EOF(self.line, self.column)
        elif char == '\n':
            return LineBreak(self.line, self.column)
        