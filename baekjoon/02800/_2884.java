import java.util.*;

class Main {

    private static void sol(int m) {
        if (m < 0) {
            System.out.println("23 " + (m + 60));
            return;
        }
        System.out.println(m / 60 + " " + m % 60);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        m = m + h * 60 - 45;
        sol(m);
        sc.close();
    }
}