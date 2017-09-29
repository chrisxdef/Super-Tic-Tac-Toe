package view;

import controller.Input;
import controller.Data;

/**
 * Created by lapost48 on 12/13/2016.
 */
public interface View {

    void display(Data data, boolean end);

    Input getInput() throws NoInputException;

    boolean hasPlayer1();

    boolean hasPlayer2();

}
