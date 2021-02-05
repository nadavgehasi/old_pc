package puzzle;

public class PuzzleSolver {
    public static void main(String[] args) {
        Piece a = new Piece(true, true,true,true, "1");
        Piece b = new Piece(true, true,true,true, "2");
        Piece c = new Piece(true, true,true,true, "3");
        Piece d = new Piece(true, true,true,true, "4");
        Puzzle puzzle = new Puzzle(2,2, a,d,c,b);
        System.out.println(puzzle.toString());
    }
}
