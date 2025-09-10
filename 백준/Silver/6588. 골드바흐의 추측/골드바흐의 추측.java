import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] notPrime = new boolean[1000001];
        notPrime[2] = false;

        for(int i=2; i*i<=1000000; i++){
            if (!notPrime[i]) {
                for (int j = i * i; j <= 1000000; j += i) {
                    notPrime[j] = true;
                }
            }
        }

        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (n != 0){

            int a = 0, b = 0;
            boolean flag = false;

            for(int i=2; i<=n/2; i++){
                if (!notPrime[i] && !notPrime[n-i]){
                    a = i;
                    b = n-i;
                    flag = true;
                    break;
                }
            }
            if (!flag) sb.append("Goldbach's conjecture is wrong.").append('\n');
            else sb.append(n + " = " + a + " + " + b).append('\n');

            n = Integer.parseInt(br.readLine());
        }
        System.out.println(sb);
    }
}
