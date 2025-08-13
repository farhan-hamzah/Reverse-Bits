class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Geser result ke kiri untuk memberi ruang bit baru
            result <<= 1
            # Ambil bit terakhir dari n
            result |= n & 1
            # Geser n ke kanan untuk ambil bit selanjutnya
            n >>= 1
        return result
