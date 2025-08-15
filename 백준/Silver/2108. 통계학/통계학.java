import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> numbers = new ArrayList<>();
        HashMap<Integer, Integer> numberCnt = new HashMap<>();
        int sum = 0;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int maxCnt = 0;
        for(int i=0; i<n; i++){
            int num = Integer.parseInt(br.readLine());
            numbers.add(num);
            sum += num;
            if (num > max) max = num;
            if (num < min) min = num;
            numberCnt.put(num, numberCnt.getOrDefault(num, 0)+1);
            if (numberCnt.get(num) > maxCnt) maxCnt = numberCnt.get(num);
        }
        Collections.sort(numbers);
        StringBuilder sb = new StringBuilder();
        sb.append(Math.round((double)sum/n)).append('\n');
        sb.append(numbers.get(n / 2)).append('\n');

        List<Integer> modeList = new ArrayList<>();
        for(Integer num : numberCnt.keySet()){
            if (numberCnt.get(num) == maxCnt) modeList.add(num);
        }
        Collections.sort(modeList);

        int mode = (modeList.size() >= 2) ? modeList.get(1) : modeList.get(0);
        sb.append(mode).append('\n');

        sb.append(Math.abs(numbers.get(n-1) - numbers.get(0)));

        System.out.println(sb);

    }
}