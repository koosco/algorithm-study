import java.io.*;
import java.util.*;

class Main {

    int[] xs = {1, -1, 0, 0};
    int[] ys = {0, 0, 1, -1};
    int n;
    int[][] graph;
    boolean[][] visited;


    private int bfs(int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        int ret = 1;

        q.offer(new int[]{i, j});
        visited[i][j] = true;

        while (!q.isEmpty()) {
            int[] p = q.poll();
            for (int d = 0; d < 4; d++) {
                int nx = p[0] + xs[d];
                int ny = p[1] + ys[d];

                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny]
                    && graph[nx][ny] == 1) {
                    q.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;
                    ret++;
                }
            }
        }
        return ret;
    }

    private void sol() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> res = new ArrayList<>();
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    res.add(bfs(i, j));
                }
            }
        }
        System.out.println(res.size());
        Collections.sort(res);
        res.forEach(System.out::println);
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}