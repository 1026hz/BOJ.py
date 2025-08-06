import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();

        word = word.replace("dz=", "1");
        word = word.replace("c=", "1");
        word = word.replace("c-", "1");
        word = word.replace("d-", "1");
        word = word.replace("lj", "1");
        word = word.replace("nj", "1");
        word = word.replace("s=", "1");
        word = word.replace("z=", "1");

        System.out.println(word.length());
    }
}
