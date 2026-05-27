import java.util.*;

public class Main {
    static ArrayList<Student> students = new ArrayList<>();
    static Scanner sc= new Scanner(System.in);

    static void addStudent() {
        System.out.print("Enter ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Name: ");
        String name =sc.nextLine();

        System.out.print("Enter Age: ");
        int age =sc.nextInt();

        System.out.print("Enter Student Class: ");
        int sclass =sc.nextInt();

        Student student= new Student(id, name, age, sclass);
        students.add(student);
        System.out.println("Student Added Successfully");
    }

    static void viewStudent() {
        if (students.isEmpty()) {
            System.out.println("No Students Found");
        } else {
            for (Student student : students) {
                student.display();
            }
        }
    }

    static void searchStudent() {
        System.out.print("Enter ID: ");
        int id= sc.nextInt();
        boolean found = false;
        for (Student student : students) {
            if (id==student.id) {
                student.display();
                found = true;
                break;
            }
        }
        if (found==false) {
            System.out.println("Student Not Found");
        }
    }

    static void updateStudent() {
        System.out.print("Enter ID: ");
        int id =sc.nextInt();
        boolean found = false;
        for (Student student : students) {
            if (id==student.id) {
                found = true;
                sc.nextLine();
                System.out.print("Enter New Name: ");
                String name = sc.nextLine();
                System.out.print("Enter New Age: ");
                int age = sc.nextInt();
                System.out.print("Enter New Class: ");
                int sclass = sc.nextInt();
                student.name = name;
                student.age = age;
                student.sclass = sclass;
                System.out.println("Updated Successfully");
                break;
            }
        }
        if (found==false) {
            System.out.println("Student Not Found");
        }
    }

    static void deleteStudent() {
        System.out.print("Enter ID: ");
        int id = sc.nextInt();
        boolean found = false;
        for (int i=0; i <students.size();i++) {
            if (id == students.get(i).id) {
                students.remove(i);
                found = true;
                System.out.println("Deleted Successfully");
                break;
            }
        }
        if (found==false) {
            System.out.println("Student Not Found");
        }
    }

    public static void main(String[] args) {

        while (true) {

            System.out.println("\n===== Student Management System =====");
            System.out.println("1. Add Student");
            System.out.println("2. View Students");
            System.out.println("3. Search Student");
            System.out.println("4. Update Student");
            System.out.println("5. Delete Student");
            System.out.println("6. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();
            switch (choice) {
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
                    System.out.println("Invalid Choice");
            }
        }
    }
}
