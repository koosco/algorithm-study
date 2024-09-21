import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {

    public void sol() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int x = Integer.parseInt(st.nextToken());
        List<Integer> nums = new ArrayList<>();
        st = new StringTokenizer(br.readLine(), " ");
        while (st.hasMoreTokens()) {
            nums.add(Integer.parseInt(st.nextToken()));
        }
        List<String> result = nums.stream()
            .filter(num -> num < x)
            .map(String::valueOf)
            .collect(Collectors.toList());
        System.out.println(String.join(" ", result));
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}