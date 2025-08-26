import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<Integer, String> pocketmon1 = new HashMap<>();
        HashMap<String, Integer> pocketmon2 = new HashMap<>();

        for(int i=1; i<=n; i++){
            String s = br.readLine();
            pocketmon1.put(i, s);
            pocketmon2.put(s, i);
        }

        for(int i=0; i<m; i++){
            String tmp = br.readLine();
            try {
                int num = Integer.parseInt(tmp);
                System.out.println(pocketmon1.get(num));
            } catch (NumberFormatException e){
                System.out.println(pocketmon2.get(tmp));
            }
        }
    }
}
