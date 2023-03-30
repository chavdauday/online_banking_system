public import java.util.Scanner;
 
class Person {
   String name;
   int age;

   public Person(){
       System.out.println("default constructor");
   }
   public Person(String name, int age) {
       this.name = name;
       this.age = age;
   }
   String getName() {
       return name;
   }
   int getAge() {
       return age;
   }
   void setName(String name) {
       this.name = name;
   }
   void setAge(int age) {
       this.age = age;
   }
   @Override
   public String toString() {
       return "Person{" + name + "age=" + age + "}";
   }
}

class Student extends Person {
   int rollno;
   double[] marks;
   static int countobject;
  
   static {
       System.out.println("static block");
       countobject = 0;
   }
   static String getcount()
   {
       return "Total Student object is " + countobject;
   }

   public Student(){
       countobject++;
       System.out.println("default constructor");
   }
   public Student(int rollno){
       countobject++;
       this.rollno = rollno;
   }
   public Student(int rollno, double[] marks) {
       countobject++;
       this.rollno = rollno;
       this.marks = marks;
   }

   public Student(int rollno,String name, int age, double[]marks){
       super(name,age);
       countobject++;
       this.rollno = rollno;
       this.marks = marks;
   }
   public int getRollno() {
       return rollno;
   }
   public void setRollno(int rollno) {
       this.rollno = rollno;
   }
   public double[] getMarks() {
           return marks;
   }
   public void setMarks(double[] marks) {
           this.marks = marks;
   }
   public String toString()
   {
       return "Student{" + "rollno= " + rollno +"}";
   }
   public void displaydeatils()
   {
       System.out.println("RollNo = " + this.rollno);
       System.out.println("Name = " + this.name);
       System.out.println("Age = " + this.age);
       for(int i = 0; i < this.marks.length; i++)
       {
           System.out.print(this.marks[i] + " ");
       }
   }
}

public   class TestStudent {
       public static void main(String[] args) {

           try (Scanner sc = new Scanner(System.in)) {
               Student[] stu = new Student[3];
               int max_mark = -1;
               int max_index = 0;
               for(int i = 0; i < stu.length; i++)
               {
                   int k=i+1;
                   stu[i] = new Student();
                   System.out.println("Enter "+ k +"'s student name");
                   stu[i].setName(sc.nextLine());
                   System.out.println("Enter "+  k +"'s student age");
                   stu[i].setAge(sc.nextInt());
                   double[] tempmark = new double[5];
                   int tempaveragemark=0;
                   for(int j=0; j<5; j++)
                   {
                       int m = j+1;
                       System.out.println("Enter "+m+ "'s subject marks");
                       double temp = sc.nextDouble();
                       tempmark[j] = temp;
                       tempaveragemark += temp;
                   }
                   stu[i].setMarks(tempmark);
                   if(max_mark < tempaveragemark)
                   {
                       max_mark = tempaveragemark;
                       max_index = i;
                   }
               }
               stu[max_index].displaydeatils();
           }
   }
}
person {
    
}
