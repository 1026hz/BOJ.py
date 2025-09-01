import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numList = new int[n+1];
        numList[0] = 0;
        numList[1] = 1;
        if (n > 1) {
            for (int i = 2; i <= n; i++) {
                numList[i] = numList[i-1] + numList[i-2];
            }
        }
        System.out.println(numList[n]);

    }
}
