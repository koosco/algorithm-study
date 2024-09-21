import java.util.*;

class Main {

    private static int sol(int x, int y) {
        if (x > 0) {
            return y > 0 ? 1 : 4;
        }
        return y > 0 ? 2 : 3;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println(sol(x, y));
    }
}