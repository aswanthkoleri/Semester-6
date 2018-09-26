/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package newlogin;

/**
 *
 * @author placements2019
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
 
 class newLogin{
    String username = "james3302";
    String password = "pass";
    String msg = " ";
      JTextField txtUsername = null;
      JTextField txtPassword = null;
     
    public static void main(String[] args){
        newLogin gui = new newLogin();
        gui.go();
    }
    public void go(){
       
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel panel = new JPanel();
        JLabel lblUsername = new JLabel("Username:");   
        JLabel lblPassword = new JLabel("Password:");
         txtUsername = new JTextField(20);
         txtPassword = new JTextField(20);
        JButton btnLogin = new JButton("Login");
        btnLogin.addActionListener(new LoginListener());
        JButton btnCancel = new JButton("Cancel");
        btnCancel.addActionListener(new CancelListener());
     
 
        panel.add(lblUsername);
        panel.add(txtUsername);
        panel.add(lblPassword);
        panel.add(txtPassword);         
        frame.getContentPane().add(BorderLayout.CENTER,panel);
 
 
 
        frame.setSize(300,300);
        frame.setVisible(true);
 
 
    }
 
    public class LoginListener implements ActionListener{
        public void actionPerformed(ActionEvent event){
            if(username.equals(txtUsername.getText())){
                if(password.equals(txtPassword.getText())){
                    msg = "Login Granted!";
                }else{
                    msg = "Login Denied";
                }
            }else{
                msg = "Login Denied";
            }   
            JOptionPane.showMessageDialog(null,msg);                    
        }
    }
    public class CancelListener implements ActionListener{
        public void actionPerformed(ActionEvent event){
            txtUsername.setText(null);
            txtPassword.setText(null);
            txtUsername.requestFocus();
        }
    }
}