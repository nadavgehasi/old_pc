package minesweeper

enum class Cell(val number: String) {
    MINE("*"),
    ZERO("0"),
    ONE("1"),
    TWO("2"),
    THREE("3"),
    FOUR("4"),
    FIVE("5"),
    SIX("6"),
    SEVEN("7"),
    EIGHT("8"),
    UNKNOWN("UNKNOWN")
}