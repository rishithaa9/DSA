import java.util.Scanner;
class Main {
    public static int gcd (int a,int b) {
        while(b!=0){
            int temp=b;
            b=a%b;
            a=temp;
        }
        return a;
        
    }
    public static void main(String[] args){
        System.out.println(gcd(10,20));
    }
}