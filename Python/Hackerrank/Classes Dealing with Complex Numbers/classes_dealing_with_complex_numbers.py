import math


class Complex(object):
    """A simple Complex number class supporting basic arithmetic.

    Operator overloading is used so that ``+``, ``-``, ``*`` and ``/``
    work directly on Complex objects, just like they do on the
    built-in numeric types. Every operation returns a *new* Complex
    object instead of modifying the operands.
    """

    def __init__(self, real, imaginary):
        # A complex number is written as "a + bi", where:
        #   - `real`     is the real part (a)
        #   - `imaginary` is the imaginary part (b) that multiplies i (i^2 = -1)
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.real + other.real,
                       self.imaginary + other.imaginary)

    def __sub__(self, other):
        # (a + bi) - (c + di) = (a - c) + (b - d)i
        return Complex(self.real - other.real,
                       self.imaginary - other.imaginary)

    def __mul__(self, other):
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        # To divide, multiply both numerator and denominator by the
        # conjugate of the denominator (c - di). The denominator then
        # becomes a real number (c^2 + d^2), which is easy to divide by:
        #
        #   (a + bi)     (a + bi)(c - di)   (ac + bd) + (bc - ad)i
        #   -------- =  ---------------- = ------------------------
        #   (c + di)     (c + di)(c - di)          c^2 + d^2
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real, imag)

    def mod(self):
        # Modulus (absolute value): |a + bi| = sqrt(a^2 + b^2).
        # The result is a real number, so the imaginary part is 0.
        # math.hypot is used instead of sqrt(a*a + b*b) because it is
        # more numerically stable (it avoids overflow/underflow).
        return Complex(math.hypot(self.real, self.imaginary), 0)

    def __str__(self):
        # Always print both parts to 2 decimal places, e.g. "3.00-4.00i".
        # The sign between the two parts is '+' when the imaginary part
        # is non-negative and '-' when it is negative. This single rule
        # also covers the special cases required by the problem:
        #   - pure real number (imaginary == 0)  -> "A+0.00i"
        #   - pure imaginary number (real == 0)  -> "0.00+Bi" or "0.00-Bi"
        real_str = "%.2f" % self.real
        # Normalise "-0.00" (produced by negative zero or tiny negatives)
        # into "0.00" so the output always looks clean.
        if real_str == "-0.00":
            real_str = "0.00"
        sign = '+' if self.imaginary >= 0 else '-'
        imag_str = "%.2f" % abs(self.imaginary)
        return "%s%c%si" % (real_str, sign, imag_str)


if __name__ == '__main__':
    # Each complex number is given on one line as "real imaginary".
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    x = Complex(a, b)
    y = Complex(c, d)

    # Required output order: C+D, C-D, C*D, C/D, mod(C), mod(D).
    results = [x + y, x - y, x * y, x / y, x.mod(), y.mod()]
    print(*(str(result) for result in results), sep='\n')
