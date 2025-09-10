import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        boolean[] numbers = new boolean[N+1];
        numbers[0] = true;
        numbers[1] = true;


        for(int i=2; i*i<=N; i++){
            if(!numbers[i]) {
                for (int j = i*i; j <= N; j += i) {
                    numbers[j] = true;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i=M; i<=N; i++){
            if(!numbers[i]) sb.append(i).append('\n');
        }
        System.out.println(sb);

    }
}
