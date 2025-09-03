import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] card = new int[]{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};

        for(int i=0; i<10; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            while (a < b) {
                int tmp = card[a];
                card[a] = card[b];
                card[b] = tmp;
                a++;
                b--;
            }

        }
        StringBuilder sb = new StringBuilder();
        for(int n : card) {
            if (n == 0) continue;
            sb.append(n).append(" ");
        }
        System.out.println(sb);

    }
}
