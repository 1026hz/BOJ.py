import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine().toUpperCase();

        int[] count = new int[26];

        for(int i=0; i<word.length(); i++){
            char now = word.charAt(i);
            count[now - 'A']++;
        }

        int max = 0;
        char ans = '?';

        for(int i=0; i<26; i++){
            if(count[i] > max){
                max = count[i];
                ans = (char)(i + 'A');
            }
            else if (count[i] == max){
                ans = '?';
            }
        }

        System.out.println(ans);

    }
}
