from re import A
from Registers import Register, FlagsRegister
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
    AF = 9
    BC = 10
    DE = 11
    HL = 12
    SP = 13

# Insturctions
class Instruction(Enum):
    #Arithmetic 
    ADCHLR8 = ArithmeticTarget.HL
    ADCR8 = ArithmeticTarget
    ADDR8 = ArithmeticTarget
    ADDHLR8 = ArithmeticTarget.HL
    ADDSP = ArithmeticTarget.SP
    ADDN8 = 1 
    ADDHLR16 = ArithmeticTarget
    ADDHLSP = ArithmeticTarget.SP
    ADDSPE8 = 2

    #Logic
    ANDR8 = ArithmeticTarget
    ANDHL = ArithmeticTarget.HL
    ANDN8 = 3

    BITR8 = ArithmeticTarget
    BITHL = ArithmeticTarget.HL

    CALLN16 = 4
    CALLCCN16 = 5

    CCF = 6

    CPR8 = ArithmeticTarget
    CPHL = ArithmeticTarget.HL
    CPN8 = 7
    CPL = ArithmeticTarget.A

    DAA = 8
    
    DECR8 = ArithmeticTarget
    DECHL = ArithmeticTarget.HL
    DECR16 = ArithmeticTarget
    DECSP = 9

    DI = 10
    EL = 11
    HALT = 12

    INCR8 = ArithmeticTarget
    INCHL = ArithmeticTarget.HL
    INCSP = 13
    
    JPN16 = 14
    JPCCN16 = 15
    JPHL = ArithmeticTarget.HL

    JRN16 = 16
    JRCCN16 = 17 

    LDR8 = ArithmeticTarget
    LDN8 = 18
    LDN16 = 19
    LDHLR8 = ArithmeticTarget
    LDHLN8 = 20
    LDR8HL = ArithmeticTarget.HL
    LDR16A = ArithmeticTarget
    LDN16A = 21
    LDHN16A = 22
    LDHCA = ArithmeticTarget.C
    LDR16 = ArithmeticTarget 
    LDHN16 = 23
    LDHC = ArithmeticTarget.C
    LDHLIA = ArithmeticTarget.HL
    LDHLDA = ArithmeticTarget.HL
    LDAHLD = ArithmeticTarget.HL
    LDAHLI = ArithmeticTarget.HL
    LDSPN16 = 24
    LDN16SP = 25
    LDHLSPE8 = ArithmeticTarget.HL
    LDSPHL = ArithmeticTarget.HL
    NOP = 26
    ORR8 = ArithmeticTarget
    ORHL = ArithmeticTarget.HL
    ORN8 = 27





class CPU(Register):
    def __init__(self):
        super().__init__()

    def execute(self, instruction: Instruction):
        # Case statement to check which instruction is being used 
        match instruction:
            case Instruction.ADDR8:
                # Case statement to check which register ADD insturction is using
                match instruction.ADDR8.value:
                    case ArithmeticTarget.C:
                        value = self.c
                        new_value = self.add(value)
                        self.a = new_value
                    case _:
                        pass


    def add(self, value: np.uint8) -> np.uint8: 
        value = self.a + value
        overflow_check = self.check_overflow_uint8(int(self.a), int(value))
        self.f.zero = True if self.a == 0 else False
        self.f.subtract = False
        self.f.carry = overflow_check
        self.f.half_carry = True if (((self.a & 0xF) + (value & 0xF)) > 0xF) else False
        return value

    def check_overflow_uint8(self, register_value: int, value: int) -> bool:
        if register_value + value > 255:
            return True
        else:
            return False 



