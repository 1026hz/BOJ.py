import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        boolean[] check = new boolean[1000001];
        StringBuilder sb = new StringBuilder();
        check[0] = true;
        check[1] = true;

        for(int i=2; i*i<=n; i++){
            if(!check[i]){
                for(int j=i*i; j<=n; j+=i){
                    check[j] = true;
                }
            }
        }

        for(int i=m; i<=n; i++){
            if (!check[i]) sb.append(i).append('\n');
        }

        System.out.println(sb);

    }
}
