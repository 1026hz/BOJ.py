import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int cntTwo = 0;
        int cntFive = 0;

        if(n>=2) {
            for (int i = 2; i <=n; i++){
                if(i % 2 == 0){
                    cntTwo += countNum(2, i);
                }
                if(i % 5 == 0){
                    cntFive += countNum(5, i);
                }
            }
        }

        System.out.println(Math.min(cntFive, cntTwo));

    }

    public static int countNum(int num, int target){
        int cnt = 0;
        while(true){
            if(target % num == 0){
                target /= num;
                cnt++;
            } else break;
        }
        return cnt;
    }
}

