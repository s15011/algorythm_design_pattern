public class Greedy {
    public static void main(String...args) {
        int change, n, sum, i;

        int val[] = { 500, 100, 50, 10, 5, 1 };

        System.out.printf("お釣りの金額は?");
        change = new java.util.Scanner(System.in).nextInt();

        //処理
        sum = 0;
        for (i = 0; i < 6; i++) {
            n = change / val[i];
            System.out.printf("%d円効果 = %d枚\n", val[i], n);
            sum += n;
            change %= val[i];
        }
        System.out.printf("硬化の合計枚数 = %d枚\n", sum);

        return;
    }
}
