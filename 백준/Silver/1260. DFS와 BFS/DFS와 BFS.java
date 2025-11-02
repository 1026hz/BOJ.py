import java.io.*;
import java.util.*;

public class Main {

    static int N,M,V;
    static List<Integer>[] graph;
    static boolean[] visited;
    static StringBuilder sb;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        sb = new StringBuilder();

        visited = new boolean[N+1];
        dfs(V);
        sb.append('\n');
        visited = new boolean[N+1];
        bfs(V);

        System.out.println(sb);

    }

    static void dfs(int start){
        visited[start] = true;
        sb.append(start).append(" ");
        for(int next : graph[start])
            if(!visited[next]) dfs(next);
    }

    static void bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        visited[start] = true;
        q.add(start);
        while (!q.isEmpty()){
            int now = q.poll();
            sb.append(now).append(" ");
            for(int next : graph[now]){
                if(!visited[next]) {
                    visited[next] = true;
                    q.add(next);
                }
            }
        }
    }
}
