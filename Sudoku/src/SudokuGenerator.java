import java.util.*;

public class SudokuGenerator {

    public static String[][] generatePuzzle() {
        int[][] grid = new int[9][9];
        fillGrid(grid);

        String[] solution = new String[9];
        char[][] puzzleChars = new char[9][9];
        for (int r = 0; r < 9; r++) {
            StringBuilder sb = new StringBuilder();
            for (int c = 0; c < 9; c++) {
                sb.append(grid[r][c]);
                puzzleChars[r][c] = (char) (grid[r][c] + '0');
            }
            solution[r] = sb.toString();
        }

        boolean Mode = MainMenu.GetMode();

        Random rand = new Random();
        int cellsToRemove = 81 - 35;
        if (Mode) {
            cellsToRemove = 81 - 20;
        }
        while (cellsToRemove > 0) {
            int r = rand.nextInt(9);
            int c = rand.nextInt(9);
            if (puzzleChars[r][c] != '-') {
                puzzleChars[r][c] = '-';
                cellsToRemove--;
            }
        }

        String[] puzzle = new String[9];
        for (int r = 0; r < 9; r++) {
            puzzle[r] = new String(puzzleChars[r]);
        }

        return new String[][] {puzzle, solution};
    }



    // ---------- Backtracking solution generator ----------
    private static boolean fillGrid(int[][] grid) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (grid[r][c] == 0) {
                    List<Integer> numbers = new ArrayList<>();
                    for (int i = 1; i <= 9; i++) numbers.add(i);
                    Collections.shuffle(numbers); // randomize order

                    for (int num : numbers) {
                        if (isSafe(grid, r, c, num)) {
                            grid[r][c] = num;
                            if (fillGrid(grid)) return true;
                            grid[r][c] = 0; // backtrack
                        }
                    }
                    return false; // no number fits
                }
            }
        }
        return true; // all cells filled
    }

    private static boolean isSafe(int[][] grid, int row, int col, int num) {
        for (int c = 0; c < 9; c++) if (grid[row][c] == num) return false;
        for (int r = 0; r < 9; r++) if (grid[r][col] == num) return false;
        int startRow = row - row % 3;
        int startCol = col - col % 3;
        for (int r = startRow; r < startRow + 3; r++)
            for (int c = startCol; c < startCol + 3; c++)
                if (grid[r][c] == num) return false;
        return true;
    }
}
