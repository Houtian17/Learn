public class is2nPower {
    static boolean is2n(int x) {
        int bitleft = Integer.numberOfLeadingZeros(x);
        int bitLength = 31 - bitleft;
        int shouldBe = 1 << bitLength;
        return (shouldBe == x);
    }
}
