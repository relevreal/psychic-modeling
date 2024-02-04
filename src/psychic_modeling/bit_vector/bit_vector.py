from array import array
from itertools import repeat


class BitVector:
    def __init__(self, n_bits):
        n_bytes = n_bits // 8
        if n_bits % 8 != 0:
            n_bytes += 1
        self._byte_array = array("B", repeat(0, n_bytes))
        self.n_bits = n_bits
        self.n_filled = 0


    def is_full(self) -> bool:
        if self.n_filled == self.n_bits:
            return True
        return False


    def __getitem__(self, key):
        if key >= self.n_bits:
            raise IndexError("bit array index out of range")
        byte_i = key // 8
        bit_i = key % 8
        byte = self._byte_array[byte_i]
        if byte & (1 << (7 - bit_i)):
            bit = 1
        else:
            bit = 0
        return bit


    def __setitem__(self, key, value):
        if key >= self.n_bits:
            raise IndexError("bit array index out of range")
        if value != 0 and value != 1:
            raise ValueError("It is a bit array, value can only be set to 0 or 1.")
        byte_i = key // 8
        bit_i = key % 8
        byte = self._byte_array[byte_i]
        curr_value = self[key]
        if value == 1 and curr_value != 1:
            byte |= (1 << (7 - bit_i))
            self._byte_array[byte_i] = byte
            self.n_filled += 1
        elif value == 0 and curr_value != 0:
            byte &= 255 - (1 << (7 - bit_i))
            self._byte_array[byte_i] = byte
            self.n_filled -= 1


    def __repr__(self) -> str:
        repr_str = "BitVector{arr}"
        arr = []
        n_bits = self.n_bits 
        for byte in self._byte_array:
            next_bits = [int(b) for b in bin(byte)[2:].zfill(8)]
            if n_bits >= 8:
                arr += next_bits 
                n_bits -= 8
            else:
                arr += next_bits[:n_bits]
                n_bits = 0
        return repr_str.format(arr=arr)
