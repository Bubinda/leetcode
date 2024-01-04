# Problem description: Given a signed (positive or negative) integer x, return x with its digits reversed. The input integer x must be in range [-2^31, 2^31 - 1] – return 0 if it isn’t.

# Seems like a simple question, but we have to think about the edge cases. The input number must be in a given range, which is obvious. But what about integers that end with a zero? For example, reversing the number 1200 should result in 21, not 0021.


def reverse_integer(x: int) -> int:
    # Integer range check
    assert -2**31 <= x <= 2**31 - 1, 'Invalid integer range'
    # Check if negative
    is_negative = True if x < 0 else False
    # Get rid of the negative sign
    if is_negative:
        x = x * -1
    # Remove trailing zeros 
    # E.g., 1200 -> 12, 12001 -> 12001
    x_rstripped = int(str(x).rstrip('0'))
    # Reverse the integer
    x_reversed = 0
    while(x_rstripped > 0):
        a = x_rstripped % 10
        x_reversed = x_reversed * 10 + a
        x_rstripped = x_rstripped // 10
        # Check if the input number was negative
    if is_negative:
        return -x_reversed
    return x_reversed
    # Test cases 
for x in [12, -12, 120, 1200, 12001]:
    print(f"IntReversed({x}) = {reverse_integer(x=x)}")
