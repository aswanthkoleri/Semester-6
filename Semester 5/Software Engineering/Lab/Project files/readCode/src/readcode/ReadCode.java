/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package readcode;
import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
/**
 *
 * @author placements2019
 */
public class ReadCode {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException {
       String INPUT="";
      String dir="sample.c";
        try {
         BufferedReader in = new BufferedReader(new FileReader(dir));
         String str;
         
         while ((str = in.readLine()) != null) {
            System.out.println(str);
            INPUT=INPUT+str+"$";
         }
         
      } catch (IOException e) {
      }
//        Now count the no of data types in the c program 
    String REGEX="\\bint\\b";
    Pattern p= Pattern.compile(REGEX);
    Matcher m=p.matcher(INPUT);
   System.out.println(INPUT);
    int count=0;
    if(m.find()){
        count++;
    }
    REGEX="\\bfloat\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    if(m.find()){
        count++;
    }
    REGEX="\\blong\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    if(m.find()){
        count++;
    }
    REGEX="\\bshort\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    if(m.find()){
        count++;
    }
    REGEX="\\bdouble\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    if(m.find()){
        count++;
    }
    REGEX="\\bunsigned\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    if(m.find()){
        count++;
    }
    REGEX="\\bsigned\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    if(m.find()){
        count++;
    }
    System.out.println("The no of data types in C code : "+count);
//  Count the number of variables of each type 
//    First number of varibales of int 
    REGEX="\\bint\\b";
    p=Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int noOfVariable=0;
    while(m.find()){
        int endIndex=m.end();
        for(int i=endIndex;INPUT.charAt(i)!=';' && INPUT.charAt(i)!='$' ;i++){
                if(INPUT.charAt(i)==','){
                    noOfVariable++;
                }
                if(INPUT.charAt(i+1)==';'){
                    noOfVariable++;
                }
        }
    }
    System.out.println("The no of INTEGER Variables : "+noOfVariable);
    REGEX="\\bfloat\\b";
    p=Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int noOfFloatVariable=0;
    while(m.find()){
        int endIndex=m.end();
        for(int i=endIndex;INPUT.charAt(i)!=';' && INPUT.charAt(i)!='$' ;i++){
                if(INPUT.charAt(i)==','){
                    noOfFloatVariable++;
                }
                if(INPUT.charAt(i+1)==';'){
                    noOfFloatVariable++;
                }
        }
    }
     System.out.println("The no of FLOAT Variables : "+noOfFloatVariable);
     REGEX="\\bdouble\\b";
    p=Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int noOfDoubleVariable=0;
    while(m.find()){
        int endIndex=m.end();
        for(int i=endIndex;INPUT.charAt(i)!=';' && INPUT.charAt(i)!='$' ;i++){
                if(INPUT.charAt(i)==','){
                    noOfDoubleVariable++;
                }
                if(INPUT.charAt(i+1)==';'){
                    noOfDoubleVariable++;
                }
        }
    }
     System.out.println("The no of Double Variables : "+noOfDoubleVariable);
     
//    Find the no of initialized variables
     REGEX="\\bint\\b";
    p=Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int noOfInitVariable=0;
    while(m.find()){
        int endIndex=m.end();
        for(int i=endIndex;INPUT.charAt(i)!=';' && INPUT.charAt(i)!='$' ;i++){
                if(INPUT.charAt(i)== '='){
                    noOfInitVariable++;
                }   
        }
    }
    System.out.println("The no of Initialized INTEGER Variables : "+noOfInitVariable);
    System.out.println("The no of UnInitialized INTEGER Variables : "+(noOfVariable-noOfInitVariable));
  
     REGEX="\\bfloat\\b";
    p=Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int noOffloatInitVariable=0;
    while(m.find()){
        int endIndex=m.end();
        for(int i=endIndex;INPUT.charAt(i)!=';' && INPUT.charAt(i)!='$' ;i++){
                if(INPUT.charAt(i)== '='){
                    noOffloatInitVariable++;
                }   
        }
    }
    System.out.println("The no of Initialized float Variables : "+noOffloatInitVariable);
    System.out.println("The no of UnInitialized float Variables : "+(noOfFloatVariable-noOffloatInitVariable));
    
 REGEX="\\bdouble\\b";
    p=Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int noOfdoubleInitVariable=0;
    while(m.find()){
        int endIndex=m.end();
        for(int i=endIndex;INPUT.charAt(i)!=';' && INPUT.charAt(i)!='$' ;i++){
                if(INPUT.charAt(i)== '='){
                    noOfdoubleInitVariable++;
                }   
        }
    }
    System.out.println("The no of Initialized double Variables : "+noOfdoubleInitVariable);
    System.out.println("The no of UnInitialized double Variables : "+(noOfDoubleVariable-noOfdoubleInitVariable));
    REGEX="\\bfor\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int forLoops=0;
    while(m.find()){
        forLoops++;
    }
    System.out.println("The no of for loops : "+forLoops);
     REGEX="\\bwhile\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int whileLoops=0;
    while(m.find()){
        whileLoops++;
    }
    System.out.println("The no of while loops : "+whileLoops);
    REGEX="\\bif\\b";
    p= Pattern.compile(REGEX);
    m=p.matcher(INPUT);
    int ifNo=0;
    while(m.find()){
        int flag=0;
        for(int i=m.end();INPUT.charAt(i)!='$';i++){
            if(INPUT.charAt(i)=='('){
                flag++;
            }else if(INPUT.charAt(i)==')'){
                flag++;
            }
        }
        if(flag==2){
        ifNo++;
        }
    }
    System.out.println("The no of if loops : "+ifNo);
    }
}
