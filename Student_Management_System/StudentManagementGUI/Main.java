import java.util.*;
import javax.swing.*;
public class Main {
    static JTextField idField;
    static JTextField nameField;
    static JTextField ageField;
    static JTextField sclassField;
    static ArrayList<Student> students = new ArrayList<>();
    /* getText()              → gets value from textbox
    Integer.parseInt()     → converts text to number
    new Student(...)       → creates student object
    students.add(...)      → stores object
    showMessageDialog()    → popup message
    setText("")            → clears input fields */
    static void addStudent() {

        int id=Integer.parseInt(idField.getText());
        String name=nameField.getText();
        int age=Integer.parseInt(ageField.getText());
        int sclass=Integer.parseInt(sclassField.getText());
        Student student=new Student(id,name,age,sclass);
        students.add(student);
        JOptionPane.showMessageDialog(null, "Student Added successfully");

    }

    static void viewStudent() {
        if (students.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Student Not Found");
        } else {
            for (Student student : students) {
                student.display();
            }
        }
    }

    static void searchStudent() {
        int id=Integer.parseInt(idField.getText());
        boolean found = false;
        for (Student student : students) {
            if (id==student.id) {
                student.display();
                found = true;
                break;
            }
        }
        if (found==false) {
            JOptionPane.showMessageDialog(null, "Student Not Found");
        }
    }

    static void updateStudent() {
        int id=Integer.parseInt(idField.getText());
        boolean found = false;
        for (Student student : students) {
            if (id==student.id) {
                found = true;
                String name=nameField.getText();
                int age=Integer.parseInt(ageField.getText());
                int sclass=Integer.parseInt(sclassField.getText());
                student.name = name;
                student.age = age;
                student.sclass = sclass;
                JOptionPane.showMessageDialog(null, "Updated Successfully");
                break;
            }
        }
        if (found==false) {
            JOptionPane.showMessageDialog(null, "Student Not Found");
        }
    }

    static void deleteStudent() {
        int id=Integer.parseInt(idField.getText());
        boolean found = false;
        for (int i=0; i <students.size();i++) {
            if (id == students.get(i).id) {
                students.remove(i);
                found = true;
                JOptionPane.showMessageDialog(null, "Deleted Successfully");
                break;
            }
        }
        if (found==false) {
            JOptionPane.showMessageDialog(null, "Student Not Found");
        }
    }

    public static void main(String[] args) {
        JFrame frame=new JFrame("Student Management System"); //title
        int width=600; //main window
        int height=600;
        frame.setSize(width,height); //setting up
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 

        frame.setLayout(null);
        //labels for inputs 
        JLabel idLabel=new JLabel("ID: "); 
        idLabel.setBounds(50,50,100,30);
        frame.add(idLabel);
        //input boxes 
        idField = new JTextField();
        idField.setBounds(150,50,150,30);
        frame.add(idField);

        JLabel nameLabel=new JLabel("Name: ");
        nameLabel.setBounds(50,100,100,30);
        frame.add(nameLabel);
        nameField = new JTextField();
        nameField.setBounds(150,100,150,30);
        frame.add(nameField);

        JLabel ageLabel=new JLabel("Age: ");
        ageLabel.setBounds(50,150,100,30);
        frame.add(ageLabel);
        ageField = new JTextField();
        ageField.setBounds(150,150,150,30);
        frame.add(ageField);

        JLabel classLabel=new JLabel("Student class: ");
        classLabel.setBounds(50,200,100,30);
        frame.add(classLabel);
        sclassField = new JTextField();
        sclassField.setBounds(150,200,150,30);
        frame.add(sclassField);

        //Buttons for operations
        JButton addButton=new JButton("Add Student");
        addButton.setBounds(50,300,120,30);
        frame.add(addButton);
        addButton.addActionListener(e -> addStudent());
        //search
        JButton searchButton=new JButton("Search Student");
        searchButton.setBounds(200,300,120,30);
        frame.add(searchButton);
        searchButton.addActionListener(e -> searchStudent());
        //update
        JButton updateButton=new JButton("Update Student");
        updateButton.setBounds(350,300,120,30);
        frame.add(updateButton);
        updateButton.addActionListener(e -> updateStudent());
        //delete
        JButton deleteButton=new JButton("Delete Student");
        deleteButton.setBounds(50,350,120,30);
        frame.add(deleteButton);
        deleteButton.addActionListener(e -> deleteStudent());
        //view all the studetns
        JButton viewButton=new JButton("View Students");
        viewButton.setBounds(200,350,120,30);
        frame.add(viewButton);
        viewButton.addActionListener(e -> viewStudent());



        frame.setVisible(true);
    }
}