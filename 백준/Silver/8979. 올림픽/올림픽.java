import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int country=0, gold=0, silver=0, bronze=0;

        int[] goldCnt = new int[n+1];
        int[] silverCnt = new int[n+1];
        int[] bronzeCnt = new int[n+1];

        for(int i=0; i<n; i++){
            st= new StringTokenizer(br.readLine());
            country = Integer.parseInt(st.nextToken());
            goldCnt[country] = Integer.parseInt(st.nextToken());
            silverCnt[country] = Integer.parseInt(st.nextToken());
            bronzeCnt[country] = Integer.parseInt(st.nextToken());
            if (country == k){
                gold = goldCnt[country];
                silver = silverCnt[country];
                bronze = bronzeCnt[country];
            }
        }

        int higher = 0;
        for(int i=1; i<=n; i++){
            if (goldCnt[i] > gold) higher++;
            else if (goldCnt[i] == gold && silverCnt[i] > silver) higher++;
            else if (goldCnt[i] == gold && silverCnt[i] == silver && bronzeCnt[i] > bronze) higher++;
        }

        System.out.println(higher + 1);

    }
}