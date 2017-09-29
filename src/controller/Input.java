package controller;

/**
 * Created by lapost48 on 12/14/2016.
 */
public class Input {

    private int[] lastClick;

    public Input(int[] lastClick) {
        this.lastClick = lastClick;
    }

    public int[] getLastClick() {
        return lastClick;
    }

}
