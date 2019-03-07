/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author aswanth
 */
import java.io.*;
import java.util.regex.*;
import java.util.*;
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader reader =  
                   new BufferedReader(new InputStreamReader(System.in)); 
        String n=reader.readLine();
        int no=Integer.parseInt(n);
        String[] arrayS=new String[no];
        for(int i=0;i<no;i++){
            arrayS[i]=reader.readLine();
        }
        int t=Integer.parseInt(reader.readLine());
        
        while(t--!=0){
//         Accept the word to find 
        String word=reader.readLine();
//         Make regex
        String REGEX="\\b"+word+"\\b";
        Pattern pat = Pattern.compile(REGEX);
            int count=0;
        for(int i=0;i<no;i++){
            Matcher mat = pat.matcher(arrayS[i]);
            while(mat.find()){
            count++;
           // System.out.println(mat.start());
            }
        }
        System.out.println(count);
        }
}
}
    