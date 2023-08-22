#!/usr/bin/env python3

class MyString:
    def __init__(self,initialValue=""):
        self._value = initialValue

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val
            
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        # Split the value using punctuation marks as delimiters
        pass

    