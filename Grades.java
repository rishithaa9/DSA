import java.util.Scanner;

public class Grades {
    public static void main(String Args[]){

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your grade A/B/C/D/F: ");
        char grade = scanner.next().toUpperCase().charAt(0);

        switch (grade){
            case 'A':
                System.out.println("Excellent");
                break;
            case 'B':
                System.out.println("Very Good");
                    break;
            case 'C':
                System.out.println("Good");
                    break;
            case 'D':
                System.out.println("=Average");
                    break; 
            case 'E':
                System.out.println("Below Average");
                    break;
            case 'F':
                System.out.println("Fail");
                    break;
            default:
                System.out.println("Invalid grade entered");    
                break;                                                   
        }
    }
    
}
