import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int bitmask = 0; // 4byte, 32bit 0이 32개 있는 상태

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String todo = st.nextToken();
            int num;

            switch (todo) {
                case "add":
                    num = Integer.parseInt(st.nextToken());
                    // |= OR 연산. num 위치를 1로 추가하는것
                    bitmask |= (1 << num);
                    break;
                case "remove":
                    num = Integer.parseInt(st.nextToken());
                    // & AND 연산
                    // ~ NOT 연산
                    // num 위치를 NOT~으로 무조건 0 만들고 & 연산으로 0만들기
                    bitmask &= ~(1 << num);
                    break;
                case "check":
                    num = Integer.parseInt(st.nextToken());
                    // 특정 비트가 1인지 &로 확인
                    sb.append((bitmask & (1 << num)) != 0 ? 1 : 0).append('\n');
                    break;
                case "toggle":
                    num = Integer.parseInt(st.nextToken());
                    // ^= XOR 연산
                    // 두 비트가 다르면 1, 같으면 0
                    // 다르면 원래 0이었다는거니까 1
                    // 같으면 원래 1이었다는거니까 0
                    bitmask ^= (1 << num);
                    break;
                case "all":
                    // 1 << 21 하면 21번째 비트만 1
                    // -1 하면 아래 20개 모두 1됨
                    bitmask = (1 << 21) - 1;
                    break;
                case "empty":
                    bitmask = 0;
                    break;
            }
        }

        System.out.print(sb);
    }
}
