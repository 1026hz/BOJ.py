import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());

        boolean[] list = new boolean[100001];
        int now = 1;

        while(true){
            if (now*now < 10001) {
                list[now*now] = true;
                now++;
            } else break;
        }

        boolean flag = false;
        int total = 0;
        int min = 0;
        for(int i=m; i<=n; i++){
            if (list[i]){
                total += i;
                if (!flag) { min=i; flag=true; }
            }
        }

        if (!flag) System.out.println(-1);
        else System.out.println(total + "\n" + min);

    }
}