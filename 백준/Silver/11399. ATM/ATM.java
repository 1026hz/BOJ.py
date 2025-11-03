import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] people = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=1; i<=N; i++){
            people[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(people);
        int sum = 0;
        int ans = 0;
        for(int i=1; i<=N; i++){
            sum += people[i];
            ans += sum;
        }

        System.out.println(ans);

    }
}