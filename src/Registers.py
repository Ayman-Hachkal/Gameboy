import numpy as np

class Register:
    def __init__(self) -> None:
        self.register = {
            'a': np.uint8(),
            'b': np.uint8(),
            'c': np.uint8(),
            'd': np.uint8(),
            'e': np.uint8(),
            'f': np.uint8(),
            'h': np.uint8(),
            'l': np.uint8(),
        }
    
    #af registers 
    def get_af(self) -> np.uint16:
        af = np.uint16(
            (self.register['a'] << 8) | self.register['f']
        )
        return af

    def set_af(self, value: np.uint16):
        self.register['a'] = np.uint8((value & 0xff00) >> 8)    #0xff00 == 1111111100000000  
        self.register['f'] = np.uint8(value & 0xff)             #0xff   == 0000000011111111


    #bc registers
    def get_bc(self) -> np.uint16:
        bc = np.uint16(
            (self.register['b'] << 8) | self.register['c']
        )
        return bc

    def set_bc(self, value: np.uint16):
        self.register['b'] = np.uint8((value & 0xff00) >> 8)
        self.register['c'] = np.uint8(value & 0xff)


    #de registers
    def get_de(self) -> np.uint16:
        de = np.uint16(
            (self.register['d'] << 8) | self.register['e']
        )
        return de

    def set_de(self, value: np.uint16):
        self.register['d'] = np.uint8((value & 0xff00) >> 8)
        self.register['e'] = np.uint8(value & 0xff)


    #hl registers
    def get_hl(self) -> np.uint16:
        hl = np.uint16(
            (self.register['h'] << 8) | self.register['l']
        )
        return hl 

    def set_hl(self, value: np.uint16):
        self.register['h'] = np.uint8((value & 0xff00) >> 8)
        self.register['l'] = np.uint8(value & 0xff)


class FlagsRegister: 
    def __init__(self) -> None:
        self.flag_register : dict[str, bool]= {
            "zero"      : bool(),
            "subtract"  : bool(),
            "half_carry": bool(), 
            "carry"     : bool()
        }
        self.ZERO_FLAG_BYTE_POSITION : int = 7
        self.SUBTRACT_FLAG_BYTE_POSITION : int = 6
        self.HALF_CARRY_FLAG_BYTE_POSITION : int = 5
        self.CARRY_FLAG_BYTE_POSITION : int = 4

    def get_flags(self) -> np.uint8: 
        return np.uint8(
            (np.uint8(1 if self.flag_register['zero'] else 0) << self.ZERO_FLAG_BYTE_POSITION) | 
            (np.uint8(1 if self.flag_register['subtract'] else 0) << self.SUBTRACT_FLAG_BYTE_POSITION) |
            (np.uint8(1 if self.flag_register['half_carry'] else 0) << self.HALF_CARRY_FLAG_BYTE_POSITION) |
            (np.uint8(1 if self.flag_register['carry'] else 0) << self.CARRY_FLAG_BYTE_POSITION)
        )

    def set_flags(self, byte: np.uint8): 
        zero : bool = bool(((byte >> self.ZERO_FLAG_BYTE_POSITION) & 1))
        subtract : bool = bool(((byte >> self.SUBTRACT_FLAG_BYTE_POSITION) & 1))
        half_carry : bool = bool(((byte >> self.HALF_CARRY_FLAG_BYTE_POSITION) & 1))
        carry : bool = bool(((byte >> self.CARRY_FLAG_BYTE_POSITION) & 1))
        self.flag_register['zero'] = zero
        self.flag_register['subtract'] = subtract 
        self.flag_register['half_carry'] = half_carry 
        self.flag_register['carry'] = carry 

