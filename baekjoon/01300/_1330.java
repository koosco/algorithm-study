import java.io.*;
import java.util.*;

class Main {
    private static String sol(int a, int b) {
        if (a > b) {
            return ">";
        }
        if (a < b) {
            return "<";
        }
        return "==";
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        System.out.println(sol(a, b));
    }
}