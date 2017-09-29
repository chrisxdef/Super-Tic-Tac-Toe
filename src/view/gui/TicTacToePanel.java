package view.gui;

import model.Player;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Created by lapost48 on 12/15/2016.
 */
class TicTacToePanel extends JPanel {

    private JButton[][] buttons;

    private int[] lastClick;
    private boolean updated;
    private int winner;

    TicTacToePanel() {
        super(new GridLayout(3, 3));
        lastClick = new int[2];
        lastClick[0] = -1;
        lastClick[1] = -1;
        updated = false;
        winner = 0;

        buttons = new JButton[3][3];
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++) {
                buttons[i][j] = createButton(i, j);
                add(buttons[i][j]);
            }
        setBorder(BorderFactory.createLineBorder(Color.BLACK));
    }

    private JButton createButton(int i, int j) {
        JButton button = new JButton();
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if(button.getText().equals("")) {
                    lastClick[0] = i;
                    lastClick[1] = j;
                    updated = true;
                }
            }
        });
        return button;
    }

    int[] getLastClick(int i, int j) {
        int[] click = lastClick;

        click[0] += i * 3;
        click[1] += j * 3;
        return click;
    }

    void setCompleted(int winner) {
        this.winner = winner;
        removeAll();
        repaint();
    }

    void reset() {
        updated = false;
    }

    public void paintComponent(Graphics g)
    {
        super.paintComponent(g);
        if(winner == 1)
            ex(g);
        if(winner == 2)
            oh(g);
        if(winner == 3)
            repaint();
    }

    public void ex(Graphics g)
    {
        g.drawLine(0, 0, getWidth(), getHeight());
        g.drawLine(0, getHeight(), getWidth(), 0);
    }

    public void oh(Graphics g)
    {
        g.drawOval(0, 0, getWidth(), getHeight());
    }

    void enableBoard(boolean enable) {
        for(JButton[] row : buttons)
            for(JButton b : row)
                b.setEnabled(enable);
    }

    void display(int[][] moves) {
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++) {
                switch(moves[i][j]) {
                    case 1:
                        buttons[i][j].setText("X");
                        break;
                    case 2:
                        buttons[i][j].setText("O");
                        break;
                    default:
                        buttons[i][j].setText("");
                }
            }
    }

    boolean isUpdated() {
        return updated;
    }

}
