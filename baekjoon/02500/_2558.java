import java.io.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int a = Integer.parseInt(br.readLine());
        String b = br.readLine();

        for (int i = 0; i < 3; i++) {
            sb.append(a * Integer.parseInt(String.valueOf(b.charAt(2 - i)))).append('\n');
        }
        sb.append(a * Integer.parseInt(b));
        System.out.println(sb);
    }
}