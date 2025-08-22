import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String isbn = br.readLine();
        int ans = 0;
        int tmp = 1;

        for(int i=0; i<13; i++){
            char c = isbn.charAt(i);
            if (c != '*') {
                int now = c - '0';
                if(i % 2 == 0) ans += now;
                else ans += 3 * now;
            } else {
                if(i % 2 == 1) tmp = 3;
            }
        }

        // 0~9 넣어서 체크
        for(int j = 0; j <= 9; j++){
            int total = ans + tmp * j;
            if(total % 10 == 0){
                System.out.println(j);
                break;
            }
        }
    }
}
