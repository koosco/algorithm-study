import java.util.*;

class Main {

    public void sol() {
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        for (int i = 1; i < 10; i++) {
            sb.append(n).append(" * ").append(i).append(" = ").append(n * i).append('\n');
        }
        System.out.println(sb);
        sc.close();
    }

    public static void main(String[] args) {
        new Main().sol();
    }
}