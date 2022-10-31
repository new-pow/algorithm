import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

		int score = Integer.parseInt(st.nextToken());
        String grade = "";
            
		if(score<=100 && score>=90) grade = "A";
		else if (score>=80) grade = "B";
		else if (score>=70) grade = "C";
		else if (score>=60) grade = "D";
		else grade = "F";
        
        System.out.println(grade);
	}
}