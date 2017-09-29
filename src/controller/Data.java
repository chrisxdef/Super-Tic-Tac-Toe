package controller;

/**
 * Created by lapost48 on 12/14/2016.
 */
public class Data {

    int winner;

    private int[][][][] subBoards;
    private int[][] subBoardWinners;

    private int openBoard;

    public Data(int[][][][] miniBoards, int[][] winners, int openBoard, int winner) {
        this.winner = winner;
        subBoards = miniBoards;
        subBoardWinners = winners;
        this.openBoard = openBoard;
    }

    public int openBoard() {
        return openBoard;
    }

    public boolean hasWinner() {
        return winner != 0;
    }

    public int getWinner() {
        return winner;
    }

    public Packet getPacket(int i, int j) {
        return new Packet(subBoards[i][j], subBoardWinners[i][j]);
    }

}
