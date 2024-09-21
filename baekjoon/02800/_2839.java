import java.util.*;

class Main {

    public void sol() throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        for (int i = (n / 5); i >= 0; i--) {
            int x = n - 5 * i;
            if (x % 3 == 0) {
                System.out.println(i + x / 3);
                return;
            }
        }
        System.out.println(-1);
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}