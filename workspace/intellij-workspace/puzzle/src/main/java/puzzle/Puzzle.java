package puzzle;

import lombok.AllArgsConstructor;

import java.util.HashMap;
import java.util.Map;

@AllArgsConstructor
public class Puzzle {
    int high;
    int width;
    Map<String, Piece> puzzle;

    public Puzzle(int high, int width, Piece... pieces) {
        puzzle = new HashMap<>();
        this.high = high;
        this.width = width;
        for (int i = 0; i < high; i++) {
            for (int j = 0; j < width; j++) {
                puzzle.put(String.format("%d%d", i, j), pieces[i  * width + j]);
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < high; i++) {
            for (int j = 0; j < width; j++) {
                stringBuilder.append(puzzle.get(String.format("%d%d", i, j)).getValue());
                stringBuilder.append(" ");
            }
            stringBuilder.append('\n');
        }
        return stringBuilder.toString();
    }
}