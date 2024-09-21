import java.util.*;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        int t =
            Integer.parseInt(st.nextToken()) * 60 + Integer.parseInt(st.nextToken()) + sc.nextInt();

        int h = t / 60;
        if (h >= 24) {
            h -= 24;
        }
        System.out.println(h + " " + (t % 60));
        sc.close();
    }
}