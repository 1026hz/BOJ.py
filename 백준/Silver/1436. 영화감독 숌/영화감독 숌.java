import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        int i = 0;
        while (n != cnt){
            i++;
            if ( Integer.toString(i).contains("666") ) cnt++;
        }
        System.out.println(i);

    }
}