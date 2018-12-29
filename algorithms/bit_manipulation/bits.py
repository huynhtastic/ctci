def get_bit(num, i):
    bit_in_place = 1 << i
    cleared_bits = num & bit_in_place
    return cleared_bits != 0

def set_bit(num, i):
    bit_in_place = 1 << i
    return bit_in_place | num

def clear_bit(num, i):
    bit_in_place = 1 << i
    return bit_in_place ^ num

def clear_bit_2(num, i):
    bit_in_place = 1 << i
    mask = ~bit_in_place
    return mask & num

def clear_msb_to_i(num, i):
    bit_in_place = 1 << i
    mask = bit_in_place - 1
    return mask & num

def clear_i_to_zero(num, i):
    bit_in_place = 1 << i
    mask = ~(bit_in_place - 1)
    return mask & num

def clear_i_to_zero_2(num, i):
    mask = (-1 << (i+1))
    return mask & num

def update_bit(num, i, bit):
    mask = ~(i << i)
    cleared_bit = num & mask
    update_bit = bit << i
    return cleared_bit | update_bit
