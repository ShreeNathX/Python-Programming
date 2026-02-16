"""
Used to perform operations at bit level (binary 0 and 1).
"""

x = 5
y = 3

print(f'{x & y}')     # AND → 1 if both bits are 1.
print(f'{x | y}')     # OR → 1 if at least one bit is 1.
print(f'{x ^ y}')     # XOR → 1 if bits are different.
print(f'{~x}')        # NOT → Inverts bits (-(x+1)).
print(f'{x << 1}')    # Left shift → Multiply by 2.
print(f'{x >> 1}')    # Right shift → Divide by 2.


"""
bitwise_operators:
  description: >
    Bitwise operators perform operations at the binary level.
    They work directly on the bits (0 and 1) of integer values.

  binary_example:
    x: 5
    y: 3
    representation:
      5: "0101"
      3: "0011"

  operators:

    AND:
      symbol: "&"
      rule: "Returns 1 only if both bits are 1."
      example:
        operation: "5 & 3"
        calculation: |
          0101
        & 0011
        -------
          0001
        result: 1

    OR:
      symbol: "|"
      rule: "Returns 1 if at least one bit is 1."
      example:
        operation: "5 | 3"
        calculation: |
          0101
        | 0011
        -------
          0111
        result: 7

    XOR:
      symbol: "^"
      rule: "Returns 1 only if bits are different."
      example:
        operation: "5 ^ 3"
        calculation: |
          0101
        ^ 0011
        -------
          0110
        result: 6

    NOT:
      symbol: "~"
      rule: >
        Inverts all bits. Python uses 2's complement representation.
        Formula: ~x = -(x + 1)
      example:
        operation: "~5"
        calculation: "-(5 + 1)"
        result: -6

    LEFT_SHIFT:
      symbol: "<<"
      rule: "Shifts bits to the left. Each shift multiplies the number by 2."
      example:
        operation: "5 << 1"
        calculation: |
          0101 → 1010
        result: 10

    RIGHT_SHIFT:
      symbol: ">>"
      rule: "Shifts bits to the right. Each shift divides the number by 2."
      example:
        operation: "5 >> 1"
        calculation: |
          0101 → 0010
        result: 2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
"""
