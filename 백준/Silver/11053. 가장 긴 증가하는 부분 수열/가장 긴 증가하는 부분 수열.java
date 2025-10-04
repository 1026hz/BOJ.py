import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> lis = new ArrayList<>();

        for(int n : arr){
            int position = Collections.binarySearch(lis, n);
            // Collections.binarySearch()
            // 찾았을 때 -> 그 인덱스
            // 못 찾았을 때 -> -(삽입할 위치 + 1)
            if(position < 0) position = -(position + 1);
            if(position == lis.size()) lis.add(n); // 제일 크면 add
            else lis.set(position, n); // 인덱스가 position인 것 n으로 바꾸기
        }

        System.out.println(lis.size());
    }
}
