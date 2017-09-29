package model;

/**
 * Created by lapost48 on 12/13/2016.
 */
class MiniBoard {

    Player winner;

    private Player[][] moves;
    private int moveCount;

    protected MiniBoard() {
        moveCount = 0;
        moves = new Player[3][3];
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++)
                moves[i][j] = Player.NONE;
        winner = Player.NONE;
    }

    private void setWinner(Player win) {
        winner = win;
    }

    public int getWinner() {
        switch(winner) {
            case X:
                return 1;
            case O:
                return 2;
            case TIE:
                return 3;
            default:
              return 0;
        }
    }

    public void update(int i, int j, int value) {
        moves[i][j] = Player.values()[value];
        moveCount++;
        checkWin();
    }

    public int[][] getValues() {
        int[][] values = new int[3][3];
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++)
                if(moves[i][j] == Player.NONE)
                    values[i][j] = 0;
                else
                    values[i][j] = (moves[i][j] == Player.X) ? 1 :  2;
        return values;
    }

    protected void checkWin() {
        Player subWinner = Player.NONE;
        for(int i = 0; i < 3; i++)
            // Check Rows
            if (moves[i][0] == moves[i][1] && moves[i][1] == moves[i][2])
                if(moves[i][0] != Player.NONE)
                    setWinner(moves[i][0]);
        for(int i = 0; i < 3; i++)
            // Check Columns
            if (moves[0][i] == moves[1][i] && moves[1][i] == moves[2][i])
                if(moves[0][i] != Player.NONE)
                    setWinner(moves[0][i]);
        // Check Diagonals
        if ((moves[0][0] == moves[1][1] && moves[1][1] == moves[2][2]) || (moves[0][2] == moves[1][1] && moves[1][1] == moves[2][0]))
            if(moves[1][1] != Player.NONE)
                setWinner(moves[1][1]);

        if(winner == Player.NONE && moveCount == 9)
            setWinner(Player.TIE);
    }

}
