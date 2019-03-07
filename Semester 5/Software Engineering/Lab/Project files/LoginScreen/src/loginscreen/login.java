/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package loginscreen;

import java.awt.*;
import javax.swing.*;
import java.util.regex.*;
import loginscreen.dash;

public class login extends JFrame {
    
    login(){
        initComponents();
    }
    private void initComponents() {
        setLayout(new FlowLayout());
        jLabel1 = new javax.swing.JLabel();
        userNameField = new javax.swing.JTextField();
        LoginButton = new javax.swing.JButton();
        resetButton = new javax.swing.JButton();
        exitButton = new javax.swing.JButton();
        passwordField = new javax.swing.JPasswordField();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jLabel1.setFont(new java.awt.Font("Ubuntu", 1, 36)); 
        jLabel1.setText("LOGIN");

        userNameField.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                userNameFieldActionPerformed(evt);
            }
        });

        LoginButton.setText("LOGIN");
        LoginButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                LoginButtonActionPerformed(evt);
            }
        });

        resetButton.setText("RESET");
        resetButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                resetButtonActionPerformed(evt);
            }
        });

        exitButton.setText("EXIT");
        exitButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                exitButtonActionPerformed(evt);
            }
        });

        passwordField.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                passwordFieldActionPerformed(evt);
            }
        });

        jLabel2.setText("Username :");

        jLabel3.setText("Password :");
         
         add(jLabel1);
         add(jLabel2);
         userNameField.setPreferredSize(new Dimension(100,30));
         add(userNameField);
         
         add(jLabel3);
         passwordField.setPreferredSize(new Dimension(100,30));
         add(passwordField);
         add(LoginButton);
         add(resetButton);
         add(exitButton);
    }
    private void LoginButtonActionPerformed(java.awt.event.ActionEvent evt) {                                            
        // TODO add your handling code here:
        String username=userNameField.getText();
        String password=passwordField.getText();
        Pattern pattern = Pattern.compile("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}");
        Matcher mat = pattern.matcher(username);
         String passwordPattern = "(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{7,}";

        if(mat.matches() && (password.matches(passwordPattern))){
            userNameField.setText(null);
            passwordField.setText(null);
            dash dashBoard=new dash();
            dashBoard.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            dashBoard.setSize(600,600);
            dashBoard.setVisible(true);
        }
        
    }                                           

    private void exitButtonActionPerformed(java.awt.event.ActionEvent evt) {                                           
        // TODO add your handling code here:
        System.exit(0);
    }                                          

    private void userNameFieldActionPerformed(java.awt.event.ActionEvent evt) {                                              
        // TODO add your handling code here:
    }                                             

    private void resetButtonActionPerformed(java.awt.event.ActionEvent evt) {                                            
                    // TODO add your handling code here:
        userNameField.setText(null);
        passwordField.setText(null);
    }                                           

    private void passwordFieldActionPerformed(java.awt.event.ActionEvent evt) {                                              
        // TODO add your handling code here:
    }   
     private javax.swing.JButton LoginButton;
    private javax.swing.JButton exitButton;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JPasswordField passwordField;
    private javax.swing.JButton resetButton;
    private javax.swing.JTextField userNameField;
}
