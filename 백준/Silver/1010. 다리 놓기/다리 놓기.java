import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        int dp[][] = new int[31][31];

        for(int i=1; i<31; i++){
            dp[i][0] = 1;
            dp[i][i] = 1;
        }

        for(int i=2; i<31; i++){
            for(int j=1; j<31; j++){
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            }
        }

        StringBuilder sb = new StringBuilder();
        StringTokenizer token;
        for(int i=0; i<t; i++){
            token = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(token.nextToken());
            int m = Integer.parseInt(token.nextToken());
            sb.append(dp[m][n]).append('\n');
        }

        System.out.println(sb);
    }
}