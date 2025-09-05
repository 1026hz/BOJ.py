import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i=1; i<=n; i++){
            String s1 = " ".repeat(n-i);
            String s2 = "*".repeat(i);
            String s3 = "*".repeat(i-1);
            sb.append(s1).append(s2).append(s3).append('\n');
        }
        for(int i=n-1; i>=1; i--){
            String s1 = " ".repeat(n-i);
            String s2 = "*".repeat(i);
            String s3 = "*".repeat(i-1);
            sb.append(s1).append(s2).append(s3).append('\n');
        }
        System.out.println(sb);
    }
}
