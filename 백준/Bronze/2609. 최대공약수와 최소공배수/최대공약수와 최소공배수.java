import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n1 = Integer.parseInt(st.nextToken());
        int n2 = Integer.parseInt(st.nextToken());

        int tmp = 0;
        int a = n1;
        int b = n2;
        while(b > 0){
            tmp = a % b;
            a = b;
            b = tmp;
        }
        int gcd = a;
        int lcm = n1*n2/gcd;

        System.out.println(gcd);
        System.out.println(lcm);



    }
}
