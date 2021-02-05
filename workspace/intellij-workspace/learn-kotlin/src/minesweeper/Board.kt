package minesweeper

class Board(private val length: Int, private val width: Int) {

    private val LOCATIONS: List<Pair<Int, Int>>  = mutableListOf(Pair(-1, -1), Pair(-1, 0), Pair(-1, 1), Pair(0, -1),
            Pair(0, 0), Pair(0, 1), Pair(1, -1), Pair(1, 0), Pair(1, 1))

    var minesLocations: MutableSet<Pair<Int, Int>> = mutableSetOf()

    fun generateMinesInBoard(numberOfMines: Int) {
        while (minesLocations.size < numberOfMines) {
            val newLocation : Pair<Int, Int> = getRandomLocation()
            minesLocations.add(newLocation)
        }
    }

    fun getBoard(): List<List<Cell>> {
        val board :MutableList<MutableList<Cell>> = mutableListOf()
        for (i in 0 until length)
            board.add(mutableListOf())

        for (i in 0 until length) {
            for (j in 0 until width) {
                board[i].add(getCellValue(Pair(i, j)))
            }
        }
        return board
    }

    private fun getRandomLocation(): Pair<Int, Int> {
        return Pair((Math.random() * 10).toInt() % length, (Math.random() * 10).toInt() % width)
    }

    private fun getCellValue(cellLocation: Pair<Int, Int>): Cell {
        if (cellLocation in minesLocations) return Cell.MINE
        return when (getNumberOfNeighbours(cellLocation)) {
            0 -> Cell.ZERO
            1 -> Cell.ONE
            2 -> Cell.TWO
            3 -> Cell.THREE
            4 -> Cell.FOUR
            5 -> Cell.FIVE
            6 -> Cell.SIX
            7 -> Cell.SEVEN
            8 -> Cell.EIGHT
            else -> Cell.UNKNOWN
        }
    }

    private fun getNumberOfNeighbours(location: Pair<Int, Int>): Int {
        return LOCATIONS.map { l -> Pair(location.first + l.first, location.second + l.second) }
                .filter { l -> l in minesLocations }.count()
    }
}