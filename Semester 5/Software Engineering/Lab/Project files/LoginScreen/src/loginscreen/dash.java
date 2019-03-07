/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package loginscreen;

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.util.UUID;
import javax.swing.table.DefaultTableModel;

/*  *
 *
 * @author placements2019
 */
public class dash extends javax.swing.JFrame {
    public dash() {
        initComponents();
    }
    
    private void initComponents(){
       jLabel1 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        dashTable = new javax.swing.JTable();
        TeamNo = new javax.swing.JTextField();
        Batch = new javax.swing.JTextField();
        PerfomanceType = new javax.swing.JTextField();
        Marks = new javax.swing.JTextField();
        Add = new javax.swing.JButton();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        jLabel1.setFont(new java.awt.Font("Ubuntu", 1, 18)); // NOI18N
        jLabel1.setText("Dashboard");
        dashTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {
                "Team number", "Batch", "Perfomance Type", "Marks","ID"
            }
            },
            new String [] {
                "Team number", "Batch", "Perfomance Type", "Marks","ID"
            }
        ));
        jScrollPane1.setViewportView(dashTable);

        Batch.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BatchActionPerformed(evt);
            }
        });

        Add.setText("Add");
        Add.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                AddActionPerformed(evt);
            }
        });

        jLabel2.setText("Team No : ");

        jLabel3.setText("Batch :");

        jLabel4.setText("Perfomance :");

        jLabel5.setText("Marks :");
         setLayout(new FlowLayout());
         add(jLabel1);
         setLayout(new FlowLayout(FlowLayout.LEFT));
         
         jLabel1.setPreferredSize(new Dimension(200,30));
         add(jScrollPane1);
         
         add(dashTable);
         setLayout(new FlowLayout(FlowLayout.LEFT));
         
         
         add(jLabel2);
         
         
         add(TeamNo);
         TeamNo.setPreferredSize(new Dimension(100,30));
         setLayout(new FlowLayout(FlowLayout.LEFT));
         add(jLabel3);
         
         add(Batch);
         Batch.setPreferredSize(new Dimension(100,30));
         setLayout(new FlowLayout(FlowLayout.LEFT));
         add(jLabel4);
         add(PerfomanceType);
         PerfomanceType.setPreferredSize(new Dimension(100,30));
         setLayout(new FlowLayout(FlowLayout.LEFT));
         add(jLabel5);
         add(Marks);
         Marks.setPreferredSize(new Dimension(100,30));
         setLayout(new FlowLayout(FlowLayout.LEFT));
         add(Add);
         
         
    }
    private void BatchActionPerformed(java.awt.event.ActionEvent evt) {                                      
        // TODO add your handling code here:
    }                                     

    private void AddActionPerformed(java.awt.event.ActionEvent evt) {                                    
        // TODO add your handling code here:
        DefaultTableModel model=(DefaultTableModel) dashTable.getModel();
        Integer i=0;
        model.addRow(new Object[]{TeamNo.getText(),Batch.getText(),PerfomanceType.getText(),Marks.getText(),UUID.randomUUID().toString()});
    }
    private javax.swing.JButton Add;
    private javax.swing.JTextField Batch;
    private javax.swing.JTextField Marks;
    private javax.swing.JTextField PerfomanceType;
    private javax.swing.JTextField TeamNo;
    private javax.swing.JTable dashTable;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JScrollPane jScrollPane1;
}
