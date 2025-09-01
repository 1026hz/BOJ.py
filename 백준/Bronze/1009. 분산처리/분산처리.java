import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for(int i=0; i<t; i++){

            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken())%10;
            int b = Integer.parseInt(st.nextToken());

            ArrayList<Integer> list = new ArrayList<>();
            list.add(a);
            int tmp = a;
            while (true){
                tmp = (tmp * a) % 10;
                if (tmp == a) break;
                else list.add(tmp);
            }

            int ans = list.get((b-1) % list.size());
            if (ans == 0) sb.append(10).append('\n');
            else sb.append(ans).append('\n');
        }

        System.out.println(sb);
    }
}
