import java.io.*;
import java.util.*;

class Main {

    BufferedReader br;
    int[] xs = {1, -1, 0, 0};
    int[] ys = {0, 0, 1, -1};

    int[][] graph = new int[50][50];
    int m, n, k;

    private void bfs(int i, int j, boolean[][] visited) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{i, j});
        visited[i][j] = true;

        while (!q.isEmpty()) {
            int[] pos = q.poll();
            for (int d = 0; d < 4; d++) {
                int nx = pos[0] + xs[d];
                int ny = pos[1] + ys[d];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny]
                    && graph[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
    }

    private void get_round() throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int x, y, res = 0;

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            y = Integer.parseInt(st.nextToken());
            x = Integer.parseInt(st.nextToken());
            graph[x][y] = 1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    bfs(i, j, visited);
                    res++;
                }
            }
        }
        System.out.println(res);
    }

    private void sol() throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            get_round();
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}