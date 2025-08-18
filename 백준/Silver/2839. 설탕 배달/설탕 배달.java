import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+6];
        dp[3] = 1;
        dp[5] = 1;

        for(int i=3; i<=n; i++){
            if (dp[i] != 0) {
                if (dp[i+3] == 0) dp[i+3] = dp[i]+1;
                if (dp[i+5] == 0) dp[i+5] = dp[i]+1;
            }
        }
        if (dp[n] == 0) System.out.println(-1);
        else System.out.println(dp[n]);

    }
}

