import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer token;

        HashMap<String, Integer> check = new HashMap<>();
        int ans = 0;

        for(int i=0; i<n; i++){
            token = new StringTokenizer(br.readLine());
            String name = token.nextToken();
            if (name.equals("ENTER")){
                check = new HashMap<>();
                continue;
            }
            if (!check.containsKey(name)) {
                check.put(name, 1);
                ans++;
            }
        }
        System.out.println(ans);
    }
}