import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] array = new int[n][2];

        StringTokenizer st;
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            array[i][0] = x;
            array[i][1] = y;
        }

        Arrays.sort(array, Comparator
                .comparingInt((int[] a) -> a[1])
                .thenComparingInt(a -> a[0]));

        StringBuilder sb = new StringBuilder();
        for (int[] a : array){
            sb.append(a[0]).append(' ').append(a[1]).append('\n');
        }
        System.out.println(sb);


    }
}

