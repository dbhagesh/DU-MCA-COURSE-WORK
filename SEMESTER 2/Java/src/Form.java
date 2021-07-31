import java.awt.*;
import java.awt.event.*;

public class Form extends Frame implements ActionListener, ItemListener {

    TextField first_name, last_name, roll_number, email;
    Checkbox male, female;
    CheckboxGroup gender;
    Choice DD, MM, YY;
    List stateList;
    Button Submit;
    TextArea text;

    public void showFrame() {
        //Layout
        setLayout(new FlowLayout());

        //Labels
        Label fname = new Label("First Name: ", Label.LEFT);
        Label lname = new Label("Last Name: ", Label.RIGHT);
        Label Gender = new Label("Gender: ", Label.LEFT);
        Label rollnum = new Label("Roll No.: ", Label.LEFT);
        Label dob = new Label("DOB: ", Label.LEFT);
        Label Email = new Label("Email id: ", Label.LEFT);
        Label Address = new Label("Address: ", Label.LEFT);
        Label state = new Label("State", Label.LEFT);
        Label submit = new Label("Submit: ", Label.CENTER);

        //TextField and Textarea
        first_name = new TextField(10);
        last_name = new TextField(10);
        roll_number = new TextField(10);
        email = new TextField(15);
        text = new TextArea(4, 15);

        //Checkbox
        gender = new CheckboxGroup();
        male = new Checkbox("Male", gender, false);
        female = new Checkbox("Female", gender, false);

        //Date Choices
        DD = new Choice();
        for(int i=1;i<=31;i++) {
            DD.add(i+"");
        }

        MM = new Choice();
        String[] month={ "Jan", "feb", "Mar", "Apr","May", "Jun", "July", "Aug","Sep", "Oct", "Nov", "Dec" };
        for(String m: month){
            MM.add(m);
        }

        YY = new Choice();
        for(int i=1995;i<2013;i++) {
            YY.add(i+"");
        }


        String[] states= {"Delhi","Mumbai","Haryana","UP","Punjab"};
        stateList = new List();
        for(String s: states){
            stateList.add(s);
        }

        //Submit
        Submit = new Button("Submit");

        //Event and Action Listeners
        male.addItemListener(this);
        female.addItemListener(this);
        first_name.addActionListener(this);
        last_name.addActionListener(this);
        roll_number.addActionListener(this);
        DD.addItemListener(this);
        MM.addItemListener(this);
        YY.addItemListener(this);
        email.addActionListener(this);
        stateList.addItemListener(this);
        Submit.addActionListener(this);
        Submit.addActionListener(this);



        add(fname);
        add(first_name);
        add(lname);
        add(last_name);
        add(Gender);
        add(male);
        add(female);
        add(rollnum);
        add(roll_number);
        add(dob);
        add(DD);
        add(MM);
        add(YY);
        add(Email);
        add(email);
        add(Address);
        add(text);
        add(state);
        add(stateList);
        add(submit);
        add(Submit);


        setSize(400, 500);
        setTitle("Form");
        setVisible(true);

    }


    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println(e);
    }

    @Override
    public void itemStateChanged(ItemEvent e) {
        System.out.println(e);
    }

    public static void main(String[] args) {

        Form form = new Form();
        form.showFrame();
    }
}
