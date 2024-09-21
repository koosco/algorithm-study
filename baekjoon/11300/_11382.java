import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long res = 0;

        for (int i=0;i<3;i++)
            res += Long.parseLong(st.nextToken());
        System.out.println(res);
    }
}