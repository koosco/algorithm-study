import java.io.*;
import java.util.*;

class Main {

    int n, m;
    int[] xs = {1, -1, 0, 0};
    int[] ys = {0, 0, 1, -1};
    int[][] graph;
    int[][] visited;

    private void bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});
        visited[0][0] = 1;

        while (!q.isEmpty()) {
            int[] pos = q.poll();
            for (int d = 0; d < 4; d++) {
                int nx = pos[0] + xs[d];
                int ny = pos[1] + ys[d];

                if (0 <= nx && nx < n &&
                    0 <= ny && ny < m &&
                    visited[nx][ny] == 0 && graph[nx][ny] == 1) {
                    visited[nx][ny] = visited[pos[0]][pos[1]] + 1;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
    }

    private void sol() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }
        bfs();
        System.out.println(visited[n-1][m-1]);
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}