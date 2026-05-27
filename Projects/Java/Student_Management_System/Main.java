//working

import java.util.*;

public class Main{
    static ArrayList<Student> students=new ArrayList<>();
    static Scanner sc =new Scanner(System.in);

    static void addStudent(){
        System.out.println("Enter ID: ");
        int id=sc.nextInt();
        sc.nextLine();
        System.out.println("Enter Name: ");
        String name=sc.nextLine();
        sc.nextLine();
        System.out.println("Enter Age: ");
        int age=sc.nextInt();
        sc.nextLine();
        System.out.println("Enter Student Class: ");
        int sclass=sc.nextInt();
        Student student=new Student(id,name,age,sclass);
        students.add(student);
        System.out.println("Student Added Successfully");
        
    }
    static void viewStudent(){
        if (students.isEmpty()){
            System.out.println("No Students Found");
        }
        else{
            for(Student student:students){
                student.display();
            }
        }
    }
    static void searchStudent(){
        System.out.println("Enter ID: ");
        int id=sc.nextInt();
        boolean found=false;
        for(Student student:students){
            if (id==student.id){
                student.display();
                found=true;
                break;
            } 
        }
        if (found==false){
                System.out.println("Student not Found");
            }

    }
    static void updateStudent(){
        System.out.println("Enter ID: ");
        int id=sc.nextInt();
        boolean found=false;
        for(Student student: students){
            if (id==student.id){
                found=true;
                System.out.println("Enter New Name:");
                String name=sc.nextLine();
                student.name=name;

                System.out.println("Enter New Age:");
                int age=sc.nextInt();
                student.age=age;

                System.out.println("Enter New Class:");
                int sclass=sc.nextInt();
                student.sclass=sclass;
                
                System.out.println("Update done");
                break;
            }
        }
        if(found==false){
            System.out.println("student Not found");
        }

    }
    static void deleteStudent(){
        System.out.println("Enter ID: ");
        int id=sc.nextInt();
        boolean found=false;

        for(int i=0;i<students.size();i++){
            if(id==students.get(i).id){
                students.remove(i);
                found=true;
                System.out.println("Deleted");
                break;
                
            }
        }
        if(found==false){
            System.out.println("Not found");
        }
    }
    public static void main(String[] args) {
        while (true){
            System.out.println("    Student Management System   ");
            System.out.println("1. Add Student ");
            System.out.println("2. View Students");
            System.out.println("3. Search Students");
            System.out.println("4. Update Student");
            System.out.println("5. Delete Student");
            System.out.println("6. Exit");

            System.out.print("Enter Choice: ");
            int choice=sc.nextInt();

            switch(choice){
                case 1:
                    addStudent();
                    break;
                case 2:
                    viewStudent();
                    break;
                case 3:
                    searchStudent();
                    break;
                case 4:
                    updateStudent();
                    break;
                case 5:
                    deleteStudent();
                    break;
                case 6:
                    System.exit(0);
                default:
                    System.out.println("Invalid");

            }
        }
    }
}