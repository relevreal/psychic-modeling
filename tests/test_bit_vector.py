from psychic_modeling.bit_vector import BitVector



def test_bit_vector():
    bv = BitVector(n_bits=128)
    assert bv.n_bits == 128
