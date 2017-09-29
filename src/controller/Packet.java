package controller;

/**
 * Created by lapost48 on 12/15/2016.
 */
public class Packet {

    private int[][] tiles;
    private int winner;

    public Packet(int[][] tiles, int winner) {
        this.tiles = tiles;
        this.winner = winner;
    }

    public int getSubWinner() {
        return winner;
    }

    public boolean isComplete() {
        return winner != 0;
    }

    public int[][] getSubBoard() {
        return tiles;
    }

}
