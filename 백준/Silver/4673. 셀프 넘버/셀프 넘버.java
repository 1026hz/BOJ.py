import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        StringBuilder sb = new StringBuilder();
        boolean[] selfNumber = new boolean[10001];

        for (int start = 1; start <= 10000; start++) {
            int tmp = start;
            int now = start;
            while (now > 0) {
                tmp += now % 10;
                now /= 10;
            }
            if (tmp <= 10000) {
                selfNumber[tmp] = true;
            }
        }

        for(int i=1; i<=10000; i++){
            if(!selfNumber[i]){
                sb.append(i).append('\n');
            }
        }
        System.out.println(sb);
    }
}