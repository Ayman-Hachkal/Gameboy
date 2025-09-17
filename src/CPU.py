import numpy as np
from enum import Enum

# Registers for the operations
class ArithmeticTarget(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    H = 7
    L = 8

# Insturctions
class Instruction(Enum):
    ADD = ArithmeticTarget



class CPU:
    def __init__(self):
        pass


    def execute(self, instruction: Instruction):
        # Case statement to check which instruction is being used 
        match instruction:
            case Instruction.ADD:
                # Case statement to check which register ADD insturction is using
                match instruction.ADD.value:
                    case ArithmeticTarget.C:
                        pass
                    case _:
                        pass

