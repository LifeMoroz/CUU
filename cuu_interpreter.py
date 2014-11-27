import os
import sys


class OP:
    def __init__(self):
        pass

    def set(self, pos):
        pass

    def get(self, pos):
        pass


class Parser:
    def __init__(self):
        self.ri = None
        self.sp = None
        self.pb = None
        self.pc = None
        self.op_readed = False
        self.r = None
        self.r1 = None
        self.r2 = None
        self.s2 = None
        self.s3 = None
        self.x = {}
        self.a = None
        self.b = None
        self.ron = []
        self.op = OP()
        self.ra = None

    @property
    def s1(self):
        return self.r1 + self.r2

    def y20(self):
        if self.op_readed:
            self.a = self.r

    def y21(self):
        if self.op_readed:
            self.a = self.s1

    def y22(self):
        if self.op_readed:
            self.a = self.s2

    def y23(self):
        if self.op_readed:
            self.a = self.s3

    def y24(self):
        self.a = self.pc

    def y25(self):
        self.a = self.pb

    def y26(self):
        self.a = self.sp

    def y27(self):
        if self.op_readed:
            self.a = self.ron[self.r1]

    def y28(self):
        if self.op_readed:
            self.a = self.ron[self.r2]

    def y29(self, pos):
        return self.ron[pos]

    def y30(self):
        return self.op.get(self.ra)

    def _operations(self, x, y, n_oper, y15=0):
        if y15:
            result = {
                0: ~x,
                1: ~(x | y),
                2: ~x & y,
                3: 0,
                4: ~(x & y),
                5: ~y,
                6: x ^ y,
                7: x & ~y,
                8: ~x | y,
                9: ~(x ^ y),
                10: y,
                11: x & y,
                12: 255,
                13: x | ~y,
                14: x | y,
                15: x
            }[n_oper]
        else:
            result = {
                0: x+1,
                1: (x << 1) + 1,
                2: x+2,
                3: None,
                4: (x >> 1),
                5: x+3,
                6: x-y,
                7: None,
                8: (x >> 1) + 8,
                9: x + y,
                10: y - x,
                11: x + 4,
                12: (x << 1),
                13: None,
                14: None,
                15: x - 1
            }[n_oper]

        self.z = bool(result)
        if result > 127:
            result -= 128
            self.c = 1
        if result < -128:
            result += 128
            self.c = 1
        if result < 0:
            self.n = 1
        return result

    def y31(self, operation):
        self.a = self._operations(self.a, self.b, operation)

    def y35(self):
        self.b = self.ri

    def y36(self):
        self.b = self.ron[self.r]

    def y37(self, operation):
        self.b = self._operations(self.a, self.b, operation)

    def y41(self, pos):
        self.ra = self.ron[pos]

    def y42(self, operation):
        self.ra = self._operations(self.a, self.b, operation)

    def y43(self):
        self.ra = 0

    def y45(self):
        self.pb = self.a

    def y47(self, x):
        self.ri += x

    def y48(self):
        self.ri = self.a


if __name__ == "__main__":
    if not os.path.isfile(sys.argv[1]):
        sys.exit(-1)