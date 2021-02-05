package minesweeper

import org.junit.jupiter.api.Test

class BoardTest {

    @Test
    fun testPrintBoard() {
        var board: Board = Board(10, 10)
        board.generateMinesInBoard(15)
        board.getBoard()
    }
}