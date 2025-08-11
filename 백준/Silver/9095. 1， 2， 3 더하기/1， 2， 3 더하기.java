import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        int[] cnt = new int[12];
        cnt[1] = 1;
        cnt[2] = 2;
        cnt[3] = 4;

        int n = 0;
        StringBuilder sb = new StringBuilder();

        for(int i=4; i<=11; i++) {
            cnt[i] = cnt[i - 1] + cnt[i - 2] + cnt[i - 3];
        }


        for(int j=0; j<t; j++){
            n = Integer.parseInt(br.readLine());
            sb.append(cnt[n]).append('\n');
        }

        System.out.println(sb);

    }
}