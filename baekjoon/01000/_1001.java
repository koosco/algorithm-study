import java.io.*;
import java.util.*;

public class _1001 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer sb = new StringTokenizer(br.readLine(), " ");

        int a = Integer.parseInt(sb.nextToken());
        int b = Integer.parseInt(sb.nextToken());

        bw.write(String.valueOf(a - b));
        bw.flush();
    }
}