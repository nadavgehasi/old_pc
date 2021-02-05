package puzzle;

import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
public class Piece {
    boolean upEdge;
    boolean downEdge;
    boolean rightEdge;
    boolean leftEdge;
    String value;
}
