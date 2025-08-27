import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, String> password = new HashMap<>();

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String url = st.nextToken();
            String pw = st.nextToken();
            password.put(url, pw);
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<m; i++){
            String tmp = br.readLine();
            sb.append(password.get(tmp)).append('\n');
        }

        System.out.println(sb);


    }
}
