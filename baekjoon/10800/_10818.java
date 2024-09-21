import java.io.*;
import java.util.*;

class Main {

    public void sol() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        List<Integer> nums = new ArrayList<>();
        while (st.hasMoreTokens()) {
            nums.add(Integer.parseInt(st.nextToken()));
        }
        int max = Collections.max(nums);
        int min = Collections.min(nums);
        System.out.println(min + " " + max);
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}