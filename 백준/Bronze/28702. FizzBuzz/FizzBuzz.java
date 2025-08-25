import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ans = 0;

        for(int i=0; i<3; i++){
            String s = br.readLine();
            if (!s.equals("FizzBuzz") && !s.equals("Fizz") && !s.equals("Buzz")){
                ans = Integer.valueOf(s) + (3-i);
                break;
            }
        }

        if (ans%3 == 0 && ans%5 == 0) System.out.println("FizzBuzz");
        else if (ans%3 == 0) System.out.println("Fizz");
        else if (ans%5 == 0) System.out.println("Buzz");
        else System.out.println(ans);
    }
}
