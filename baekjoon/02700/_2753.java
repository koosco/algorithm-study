import java.util.*;

class Main {

    private static int sol(int y) {
        if (y % 4 != 0) {
            return 0;
        }
        if (y % 100 != 0 || y % 400 == 0) {
            return 1;
        }
        return 0;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        System.out.println(sol(year));
        sc.close();
    }
}