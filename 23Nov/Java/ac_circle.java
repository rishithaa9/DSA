// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        
        System.out.print("Enter Radius: ");
        int r = sc.nextInt();
        float pi = 3.14f ;
        float area= pi * (r * r ) ;
        System.out.println("Area: "+ area);
    }
}