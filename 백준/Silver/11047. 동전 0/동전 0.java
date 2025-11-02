import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] coins = new int[N + 1];
        int ans = 0;

        for (int i = 1; i <= N; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        for (int i = N; i >= 1; i--) {
            if(K >= coins[i]){
                ans += K/coins[i];
                K %= coins[i];
            }
            if(K == 0) break;
        }

        System.out.println(ans);
    }
}