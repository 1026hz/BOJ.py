import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] numbers = new int[N+1];

        st = new StringTokenizer(br.readLine());
        int sum = 0;
        for(int i=1; i<=N;i++){
            sum += Integer.parseInt(st.nextToken());
            numbers[i] = sum;
        }

        StringBuilder sb = new StringBuilder();
        for(int x=0; x<M; x++){
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            sb.append(numbers[j] - numbers[i-1]).append('\n');
        }

        System.out.println(sb);

    }
}
