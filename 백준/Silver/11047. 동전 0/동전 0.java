import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int cnt = 0;

        List<Integer> coins = new ArrayList<>();

        for(int i=0; i<n; i++){
            coins.add(Integer.parseInt(br.readLine()));
        }

        coins.sort(Comparator.reverseOrder());

        for(int i : coins){
            while (k >= i) {
                cnt++;
                k -= i;
            }
        }
        System.out.println(cnt);

    }
}
