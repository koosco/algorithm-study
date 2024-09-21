import java.util.*;

class Main {

    private static char sol(int s) {
        if (s >= 90) {
            return 'A';
        }
        if (s >= 80) {
            return 'B';
        }
        if (s >= 70) {
            return 'C';
        }
        if (s >= 60) {
            return 'D';
        }
        return 'F';
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();
        System.out.println(sol(score));
        sc.close();
    }
}