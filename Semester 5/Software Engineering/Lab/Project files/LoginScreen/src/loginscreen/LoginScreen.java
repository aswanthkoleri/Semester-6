/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package loginscreen;
import javax.swing.JFrame;
import loginscreen.login;
/**
 *
 * @author placements2019
 */
public class LoginScreen {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        login gui= new login();
        gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        gui.setSize(200,200);
        gui.setVisible(true);
        gui.setTitle("LOGIN");
    }
    
}
