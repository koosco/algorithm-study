import java.util.*;

class Main {

    public void sol() throws Exception {
        Scanner sc = new Scanner(System.in);
        int max = 0, idx = 0;
        for (int i = 1; i < 10; i++) {
            int x = sc.nextInt();
            if (x > max) {
                max = x;
                idx = i;
            }
        }
        System.out.println(max + "\n" + idx);
        sc.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}