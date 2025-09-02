import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int x = String.valueOf(n).length();

        if (x==1) System.out.println(n);
        else if (x==2) System.out.println(9 + (n-9) * 2 );
        else if (x==3) System.out.println(9 + 90 * 2 + (n-99) * 3 );
        else if (x==4) System.out.println(9 + 90 * 2 + 900 * 3 + (n-999) * 4);
        else if (x==5) System.out.println(9 + 90 * 2 + 900 * 3 + 9000 * 4 + (n-9999) * 5);
        else if (x==6) System.out.println(9 + 90 * 2 + 900 * 3 + 9000 * 4 + 90000 * 5 + (n-99999) * 6);
        else if (x==7) System.out.println(9 + 90 * 2 + 900 * 3 + 9000 * 4 + 90000 * 5 + 900000 * 6 + (n-999999) * 7);
        else if (x==8) System.out.println(9 + 90 * 2 + 900 * 3 + 9000 * 4 + 90000 * 5 + 900000 * 6 + 9000000 * 7 + (n-9999999) * 8);
        else if (x==9) System.out.println(9 + 90 * 2 + 900 * 3 + 9000 * 4 + 90000 * 5 + 900000 * 6 + 9000000 * 7 + 90000000 * 8 + (n-99999999) * 9);

    }
}