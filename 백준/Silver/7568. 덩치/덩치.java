import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int[][] array = new int[n+1][2];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            array[i][0] = Integer.parseInt(st.nextToken());
            array[i][1] = Integer.parseInt(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<n; i++){
            int rank = 1;
            for(int j=0; j<n; j++){
                if (i != j){
                    if(array[i][0] < array[j][0] && array[i][1] < array[j][1]){
                        rank++;
                    }
                }
            }
            sb.append(rank).append(' ');
        }

        System.out.println(sb);

    }
}

