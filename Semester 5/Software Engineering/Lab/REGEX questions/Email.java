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
        
//         Accept the word to find 
        
//         Make regex
        String REGEX="\\b\\S+@\\w+(\\.\\w+)+\\b";
        Pattern pat = Pattern.compile(REGEX);
            int count=0;
        
        for(int i=0;i<no;i++){
            Matcher mat = pat.matcher(arrayS[i]);
            while(mat.find()){
            count++;    
            }
        }
        String[] result=new String[count];
        int j=0;
         for(int i=0;i<no;i++){
            Matcher mat = pat.matcher(arrayS[i]);
            while(mat.find()){
            result[j]=mat.group();
                j++;
            }
         }
       
        // for( j=0;j<count;j++){
        //     System.out.println(result[j]);
        // }
        //  System.out.println("");
        
        for(int i=0;i<count-1;i++){
            for(j=i+1;j<count;j++){
                if(result[i].compareTo(result[j])>0){
//                     Swap
                    String temp=result[i];
                    result[i]=result[j];
                    result[j]=temp;
                }
            }
        }
         Set<String> temp = new LinkedHashSet<String>( Arrays.asList(result ) );
       String[] answer = temp.toArray( new String[temp.size()] );
        // java.util.Set set = new java.util.HashSet(java.util.Arrays.asList(result));
         for( j=0;j<answer.length-1;j++){
            System.out.print(answer[j]+";");
        }
        System.out.print(answer[j]);
        // System.out.println(count);
       
}
}