public class Count{
    public static void main(String...args) {
        Sfmt sfmt = new Sfmt(256);
        for (int a = 0; a < 10; a++) {
            int b = (byte)sfmt.NextInt(256);
            int c = 0;
            String str = Integer.toBinaryString(b);
                for (int i = 0; i < str.length(); i++){
                    if (str.charAt(i) == '1');
                    c++;
                }
            System.out.println(b + "の1の個数は" + c);
        }
    }
}
