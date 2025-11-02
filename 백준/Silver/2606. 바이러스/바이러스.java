import java.io.*;
import java.util.*;

public class Main {

    static int N, M, ans;
    static List<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        graph = new List[N+1];
        for(int i=0; i<=N; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<M; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        visited = new boolean[N+1];
        bfs(1);
        System.out.println(ans);

    }

    static void bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        ans = 0;
        while(!q.isEmpty()){
            int now = q.poll();
            visited[now] = true;
            for(int next : graph[now]){
                if (!visited[next]) {
                    visited[next] = true;
                    q.add(next);
                    ans++;
                }
            }
        }
    }

}
