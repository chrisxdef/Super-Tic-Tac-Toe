package controller;

import model.Model;
import model.Board;
import view.NoInputException;
import view.View;
import view.gui.GUIView;

/**
 * Created by lapost48 on 12/13/2016.
 */
public class Controller {

    private static View view = new GUIView(true, true);

    private static boolean gameWin = false;

    private static Model model = new Board();
    private static boolean player1Turn = true;

    public static void main(String[] args) {

        Data data = model.getData();

        while(!gameWin) {
            view.display(data, false);

            // Get input from proper sources
            Input input = null;
            try {
                if(player1Turn) {
                    if (view.hasPlayer1())
                        input = view.getInput();
                } else {
                    if (view.hasPlayer2())
                        input = view.getInput();
                }
            } catch(NoInputException e) {
                continue;
            }
            if(input == null)
                input = aiInput(data);

            model.update(input, player1Turn);

            data = model.getData();
            gameWin = data.hasWinner();

            toggleTurnPlayer();
        }

        view.display(data, true);
        endGame(data);

    }

    private static Input aiInput(Data data) {
        // Call python script and get two numbers from 0-8 that represents which square the AI wants to choose
        return null;
    }

    private static void toggleTurnPlayer() {
        player1Turn = !player1Turn;
    }

    private static void endGame(Data data) {
        System.out.println(data.getWinner());
    }

}
