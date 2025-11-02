import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static List<Integer> ans = new LinkedList<>();
    static List<Integer>[] graph;
    static boolean[][] visited;
    static int[][] map;
    static int dx[] = {-1, 1, 0, 0};
    static int dy[] = {0, 0, -1, 1};

    static class Node{
        int x, y;
        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        map = new int[N+2][N+2];
        for(int i=1; i<=N; i++){
            String line = br.readLine();
            for(int j=1; j<=N; j++){
                map[i][j] = line.charAt(j-1) - '0';
            }
        }

        visited = new boolean[N+2][N+2];
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                if(!visited[i][j] && map[i][j] == 1) bfs(i, j);
            }
        }

        Collections.sort(ans);
        StringBuilder sb = new StringBuilder();
        sb.append(ans.size()).append('\n');
        for(int i : ans){
            sb.append(i).append('\n');
        }
        System.out.println(sb);

    }

    static void bfs(int x, int y){
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(x, y));
        visited[x][y] = true;
        int nowCnt=1;

        while(!q.isEmpty()){
            Node now = q.poll();
            for(int i=0; i<4; i++){
                int nowX = now.x + dx[i];
                int nowY = now.y + dy[i];

                if(!visited[nowX][nowY] && map[nowX][nowY]==1){
                    q.add(new Node(nowX, nowY));
                    visited[nowX][nowY] = true;
                    nowCnt++;
                }
            }
        }
        ans.add(nowCnt);
    }


}
