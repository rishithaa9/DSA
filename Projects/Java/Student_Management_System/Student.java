class Student{
    int id;
    String name;
    int age;
    int sclass;
    Student(int id,String name,int age,int sclass){
        this.id=id;
        this.name=name;
        this.age=age;
        this.sclass=sclass;

    }
    void display(){
        System.out.println("ID: "+id);
        System.out.println("Name: " +name);
        System.out.println("Age: "+age);
        System.out.println("Student Class: " +sclass);
    }
}