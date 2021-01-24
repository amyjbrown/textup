"""
Token 
This Module is designed to be wildcard imported
Type Token:
    abstract dataclass used for descirbing a token for the lexer 
"""
__all__ = ['Token', 'Number', 'Word', 'LineBreak', 'Comma', 'LBracket', 'RBracket', 'EOF']

from dataclasses import dataclass

@dataclass
class Token: 
    line: int 
    column: int

    def word(self) -> 'Word': # this is reverse comptabile, and will be handled by various functoins that need it
        """
        Converts Token to word, as used in the parser
        """
        raise NotImplementedError(f'{self} cannot be converted to word')

@dataclass
class Number(Token):
    value: float
    
    def word(self) -> 'Word':
        return Word(self.line, self.column, str(self.value))

@dataclass
class Word(Token):
    text: str 
    def word(self) -> 'Word': 
        return self

class LineBreak(Token): pass

class LBracket(Token): 
    def word(self) -> 'Word':
        return Word(self.line, self.column, '<')


class RBracket(Token): 
    def word(self) -> 'Word':
        return Word(self.line, self.column, '>')


class Comma(Token): 
    def word(self) -> 'Word':
        return Word(self.line, self.column, ',')


class EOF(Token): pass