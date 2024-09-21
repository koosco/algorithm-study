import java.util.*;
import java.lang.Math;
class Main {

    public int sol() {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        sc.close();
        if (a == b && b == c) {
            return 10_000 + a * 1_000;
        }
        if (a == b || b == c) {
            return 1_000 + b * 100;
        }
        if (a == c) {
            return 1_000 + a * 100;
        }
        return Math.max(a, Math.max(b, c)) * 100;
    }

    public static void main(String[] args) {
        System.out.println(new Main().sol());
    }
}