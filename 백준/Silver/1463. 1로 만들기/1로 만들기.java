import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1];

        for(int i=2; i<=n; i++){
            int min = dp[i - 1];
            if(i % 2 == 0 && dp[i / 2] < min){
                min = dp[i / 2];
            }
            if(i % 3 == 0 && dp[i / 3] < min){
                min = dp[i / 3];
            }
            dp[i] = min + 1;
        }
        System.out.println(dp[n]);
    }
}