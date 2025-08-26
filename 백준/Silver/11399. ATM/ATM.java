import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] people = new int[n];
        int now = 0;
        int ans = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            int tmp = Integer.parseInt(st.nextToken());
            people[i] = tmp;
        }
        Arrays.sort(people);

        for(int i=0; i<n; i++){
            now += people[i];
            ans += now;
        }

        System.out.println(ans);

    }
}
