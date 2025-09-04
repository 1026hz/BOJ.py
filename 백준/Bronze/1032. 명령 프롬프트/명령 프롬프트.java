import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        String s = br.readLine();
        char[] arr = s.toCharArray();
        int num = arr.length;
        char[] ans = arr;

        for(int i=1; i<n; i++){
            String tmp = br.readLine();
            char[] tmpArr = tmp.toCharArray();
            for(int j=0; j<num; j++){
                if (arr[j] != tmpArr[j]) ans[j]='?';
            }
        }

        StringBuilder sb = new StringBuilder();
        for(char c : ans){
            sb.append(c);
        }
        System.out.println(sb);


    }
}
