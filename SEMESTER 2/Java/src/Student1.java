

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Student1 {
    int roll_number;
    String student_name;
    String[] marks;

    Student1() throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("Enter Student roll number : ");
        roll_number=Integer.parseInt(br.readLine());

        System.out.println("Enter Student name : ");
        student_name=br.readLine();

        System.out.println("Enter space separated marks of student : ");
        marks = br.readLine().split(" ");

        for(String mark : marks) {
            if (Integer.parseInt(mark) < 40) {
                throw new NotPassedException();
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            try {
                new Student1();

            }
            catch(Exception e) {
                System.out.println("Exception : " + e);
            }
            finally {
                System.out.println("Enter 1 to exit :   ");
                if(br.readLine().equals("1")) {
                    break;
                }
            }



        }
    }


}
class NotPassedException extends Exception{

    private static final long serialVersionUID = 1L;
    NotPassedException(){
        super("Marks are not sufficient/Fail");
    }
}

