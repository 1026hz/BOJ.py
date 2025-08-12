import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer token;

        Set<String> check = new HashSet<>();
        int ans = 0;

        for(int i=0; i<n; i++){
            token = new StringTokenizer(br.readLine());
            String name = token.nextToken();
            if (name.equals("ENTER")){
                ans += check.size();
                check = new HashSet<>();
            } else {
                check.add(name);
            }
        }
        ans += check.size();
        System.out.println(ans);
    }
}