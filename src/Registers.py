import numpy as np
from dataclasses import dataclass

@dataclass
class FlagsRegister: 
    zero      : bool = False
    subtract  : bool = False
    half_carry: bool = False
    carry     : bool = False
    ZERO_FLAG_BYTE_POSITION : int = 7
    SUBTRACT_FLAG_BYTE_POSITION : int = 6
    HALF_CARRY_FLAG_BYTE_POSITION : int = 5
    CARRY_FLAG_BYTE_POSITION : int = 4

    def get_flags(self) -> np.uint8: 
        return np.uint8(
            (np.uint8(1 if self.zero else 0) << self.ZERO_FLAG_BYTE_POSITION) | 
            (np.uint8(1 if self.subtract else 0) << self.SUBTRACT_FLAG_BYTE_POSITION) |
            (np.uint8(1 if self.half_carry else 0) << self.HALF_CARRY_FLAG_BYTE_POSITION) |
            (np.uint8(1 if self.carry else 0) << self.CARRY_FLAG_BYTE_POSITION)
        )

    def set_flags(self, byte: np.uint8): 
        zero : bool = bool(((byte >> self.ZERO_FLAG_BYTE_POSITION) & 1))
        subtract : bool = bool(((byte >> self.SUBTRACT_FLAG_BYTE_POSITION) & 1))
        half_carry : bool = bool(((byte >> self.HALF_CARRY_FLAG_BYTE_POSITION) & 1))
        carry : bool = bool(((byte >> self.CARRY_FLAG_BYTE_POSITION) & 1))
        self.zero = zero
        self.subtract = subtract 
        self.half_carry = half_carry 
        self.carry = carry 

@dataclass
class Register:
    a: np.uint8 = np.uint8(0)
    b: np.uint8 = np.uint8(0) 
    c: np.uint8 = np.uint8(0)
    d: np.uint8 = np.uint8(0)
    e: np.uint8 = np.uint8(0)
    f = FlagsRegister()
    h: np.uint8 = np.uint8(0)
    l: np.uint8 = np.uint8(0)
    sp : np.uint16 = np.uint16(0)
    
    #af registers 
    def get_af(self) -> np.uint16:
        af = np.uint16(
            (self.a << 8) | self.f.get_flags()
        )
        return af

    def set_af(self, value: np.uint16):
        self.a = np.uint8((value & 0xff00) >> 8)    #0xff00 == 1111111100000000  
        self.f.set_flags(np.uint8(value & 0xff))             #0xff   == 0000000011111111


    #bc registers
    def get_bc(self) -> np.uint16:
        bc = np.uint16(
            (self.b << 8) | self.c
        )
        return bc

    def set_bc(self, value: np.uint16):
        self.b = np.uint8((value & 0xff00) >> 8)
        self.c = np.uint8(value & 0xff)


    #de registers
    def get_de(self) -> np.uint16:
        de = np.uint16(
            (self.d << 8) | self.e
        )
        return de

    def set_de(self, value: np.uint16):
        self.d = np.uint8((value & 0xff00) >> 8)
        self.e = np.uint8(value & 0xff)


    #hl registers
    def get_hl(self) -> np.uint16:
        hl = np.uint16(
            (self.h << 8) | self.l
        )
        return hl 

    def set_hl(self, value: np.uint16):
        self.h = np.uint8((value & 0xff00) >> 8)
        self.l = np.uint8(value & 0xff)


