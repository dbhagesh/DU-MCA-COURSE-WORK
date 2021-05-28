package com.ducs;
import java.util.*;
public class Main {

    public static void main(String[] args) {
        /*
        Input from the user:
        Must be odd value
        (n-1)/2 lines: include the upper part
        1 line       : middle line
        (n-1)/2 lines: include the lower part
        ______________
        =n lines

        Figure to be printed:
           *      -|
           **      |Upper portion
           ***     |
           ****   -|
        ********* ->Middle line
           ****   -|
           ***     |
           **      |Lower portion
           *      -|

         */
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter any value - ");
        int n = sc.nextInt();
        //Right limit
        int r = (n-1)/2;

        //Upper figure
        for(int i=1; i<=r; i++){
            //Making r-1 spaces on left of each line
            for(int k=0; k<r-1; k++){
                System.out.print(" ");
            }
            //Printing *
            for(int j=0; j<i; j++){
                System.out.print("*");
            }
            System.out.println("");
        }
        //Middle line
        for(int i=0; i<n; i++){
            System.out.print("*");
        }
        System.out.println("");

        //Lower Figure
        for(int i=r; i>=1; i--){
            //Making r-1 spaces on left of each line
            for(int k=0; k<r-1; k++){
                System.out.print(" ");
            }
            //Printing *
            for(int j=0; j<i; j++){
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}
