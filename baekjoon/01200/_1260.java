import java.util.*;
import java.util.stream.*;
import java.io.*;

class Main {
    int n, m, v;
    int s, e;
    HashMap<Integer, List<Integer>> graph = new HashMap<>();
    List<Integer> dfs_res = new ArrayList<>();
    boolean[] visited;

    private void init_visited() {
        visited = new boolean[n + 1];
    }

    private void dfs(int x) {
        visited[x] = true;
        dfs_res.add(x);
        for (int v : graph.get(x)) {
            if (!visited[v]) {
                dfs(v);
            }
        }
    }


    private List<Integer> bfs(int start_v) {
        Queue<Integer> q = new LinkedList<>();
        List<Integer> ret = new ArrayList<>();

        q.offer(start_v);
        visited[start_v] = true;
        ret.add(start_v);

        while (!q.isEmpty()) {
            int x = q.poll();
            for (int v : graph.get(x)) {
                if (!visited[v]) {
                    q.offer(v);
                    visited[v] = true;
                    ret.add(v);
                }
            }
        }
        return ret;
    }

    private void sol() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        init_visited();

        for (int i = 1; i <= n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
                graph.get(s).add(e);
                graph.get(e).add(s);
        }

        for (List<Integer> val : graph.values()) {
            Collections.sort(val);
        }

        init_visited();
        dfs(v);
        System.out.println(dfs_res.stream().map(String::valueOf).collect(Collectors.joining(" ")));

        init_visited();
        System.out.println(bfs(v).stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}