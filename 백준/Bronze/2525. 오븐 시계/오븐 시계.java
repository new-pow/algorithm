import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int hour = sc.nextInt();
		int min = sc.nextInt();
		int cookTime = sc.nextInt();
		
		if (min+cookTime < 60) {
			min += cookTime;
		} else if (min+cookTime >= 60) {
			hour += (min+cookTime)/60;
			min = (min+cookTime)%60;
		}
		
		if (hour>=24) hour-=24;
		
		System.out.println(hour+" "+min); }}