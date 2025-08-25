import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            Queue<int[]> q = new LinkedList<>();  // 일반 큐
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()); // max 보기 위핸 우선순위큐, 내림차순으로 받음

            for (int i = 0; i < n; i++) {
                int priority = Integer.parseInt(st.nextToken());
                q.offer(new int[]{i, priority});  // (문서번호, 중요도)
                pq.offer(priority);              // 중요도 우선순위 저장
            }

            int count = 0;
            while (!q.isEmpty()) {
                int[] now = q.poll();

                // 현재 문서가 가장 높은 중요도가 아니라면 다시 큐에 넣음
                if (now[1] < pq.peek()) {
                    q.offer(now);
                } else {
                    pq.poll();
                    count++;
                    if (now[0] == m) {
                        System.out.println(count);
                        break;
                    }
                }
            }
        }
    }
}
