class Solution:
    def getbin(self, num):
            bins = []
            while num > 0:
                bins += [num%2]
                num >>= 1

            return bins[::-1]

    def bin2int(self, bins):
        exp, _sum = 0, 0
        while bins:
            _sum += bins.pop() * (2**exp)
            exp += 1

        return _sum

    def bitwiseComplement(self, N: int) -> int:
        print([0 if b else 1 for b in self.getbin(N)])
        return self.bin2int([0 if b else 1 for b in self.getbin(N)]) if N else 1
