package view.gui;

import controller.Data;
import controller.Input;
import controller.Packet;
import view.NoInputException;
import view.View;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Created by lapost48 on 12/14/2016.
 */
public class GUIView extends JFrame implements View {

    private boolean guiPlayer1;
    private boolean guiPlayer2;

    private TicTacToePanel[][] panels;

    private int[] lastClick;
    private boolean newInput;

    public GUIView(boolean p1, boolean p2) {
        guiPlayer1 = p1;
        guiPlayer2 = p2;

        panels = new TicTacToePanel[3][3];
        lastClick = new int[2];
        lastClick[0] = -1;
        lastClick[1] = -1;
        newInput = false;
        initFrame();
    }

    private void initFrame() {
        setTitle("Super Tic Tac Toe");
        setLayout(new GridLayout(3, 3));
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++) {
                panels[i][j] = new TicTacToePanel();
                add(panels[i][j]);
            }
        setSize(500, 500);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    private boolean hasInput() {
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++) {
                if(panels[i][j].isUpdated()) {
                    newInput = true;
                    lastClick = panels[i][j].getLastClick(i, j);
                    panels[i][j].reset();
                }
            }
        return newInput;
    }

    public Input getInput() throws NoInputException {
        if(hasInput()) {
            newInput = false;
            return new Input(lastClick);
        }
        throw new NoInputException();
    }

    public void display(Data data, boolean end) {
        int openBoard = data.openBoard();
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++) {
                Packet p = data.getPacket(i, j);
                if(p.isComplete())
                    panels[i][j].setCompleted(p.getSubWinner());
                else {
                    if(end || openBoard != 9 && openBoard != (3 * i) + j)
                        panels[i][j].enableBoard(false);
                    else
                        panels[i][j].enableBoard(true);
                    panels[i][j].display(p.getSubBoard());
                }
            }
    }

    public boolean hasPlayer1() {
        return guiPlayer1;
    }

    public boolean hasPlayer2() {
        return guiPlayer2;
    }

}
