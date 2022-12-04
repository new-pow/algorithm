
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static LinkedList<Integer> linkedList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        linkedList = new LinkedList<>();

        for (int i=0; i<n; i++) {
            linkedList.add(i+1);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        int index = 0;
        while (linkedList.size()>1) {
            for (int i=0; i<k-1; i++) {
                linkedList.add(linkedList.remove(0));
            }
            sb.append(linkedList.remove(0)+", ");
        }

        sb.append(linkedList.remove(0)+">");

        System.out.println(sb.toString());
    }
}
