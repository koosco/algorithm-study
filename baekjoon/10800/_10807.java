import java.io.*;
import java.util.*;

class Main {
    public void sol() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Integer.parseInt(br.readLine());
        List<Integer> nums = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        while (st.hasMoreTokens()) {
            nums.add(Integer.parseInt(st.nextToken()));
        }
        int v = Integer.parseInt(br.readLine());

        System.out.println(Collections.frequency(nums, v));
    }

    public static void main(String[] args) throws Exception{
        new Main().sol();
    }
}