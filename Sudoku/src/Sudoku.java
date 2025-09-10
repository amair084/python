import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Sudoku {
    static class Tile extends JButton {
        int r;
        int c;
        Tile(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    int boardWidth = 600;
    int boardHeight = 650;

    String[][] puzzleAndSolution = SudokuGenerator.generatePuzzle();
    String[] puzzle = puzzleAndSolution[0];
    String[] solution = puzzleAndSolution[1];

    JFrame frame = new JFrame("Sudoku");
    JLabel textLabel = new JLabel();
    JPanel textPanel = new JPanel();
    JPanel boardPanel = new JPanel();
    JPanel buttonsPanel = new JPanel();

    JButton numSelected = null;
    int errors = 0;



    Sudoku() {
        frame.setSize(boardWidth, boardHeight);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setLayout(new BorderLayout());

        textLabel.setFont(new Font("Arial", Font.BOLD, 30));
        textLabel.setHorizontalAlignment(JLabel.CENTER);
        textLabel.setText("Sudoku: 0");

        textPanel.add(textLabel);
        frame.add(textPanel, BorderLayout.NORTH);

        boardPanel.setLayout(new GridLayout(9, 9));
        setupTiles();

        frame.add(boardPanel);

        buttonsPanel.setLayout(new GridLayout(1, 9));
        setupButtons();
        frame.add(buttonsPanel, BorderLayout.SOUTH);

        frame.setVisible(true);

    }

    void setupTiles() {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                Tile tile = new Tile(r, c);
                char titleChar = puzzle[r].charAt(c);

                if (titleChar == '-') {
                    tile.setText("");
                    tile.setBackground(Color.WHITE);
                } else {
                    tile.setText(String.valueOf(titleChar));
                    tile.setBackground(Color.lightGray);
                }

                tile.setFocusable(false);

                tile.setPreferredSize(new Dimension(60, 60));
                tile.setFont(new Font("Arial", Font.BOLD, 20));
                if (r == 2 && c == 2 || r == 2 && c == 5 || r == 5 && c == 2 || r == 5 && c == 5) {
                    tile.setBorder(BorderFactory.createMatteBorder(1,1,5,5,Color.BLACK));
                } else if (r == 2 || r == 5) {
                    tile.setBorder(BorderFactory.createMatteBorder(1,1,5,1,Color.BLACK));
                } else if (c == 2 || c == 5) {
                    tile.setBorder(BorderFactory.createMatteBorder(1,1,1,5,Color.BLACK));
                } else {
                    tile.setBorder(BorderFactory.createLineBorder(Color.black));
                }

                boardPanel.add(tile);

                tile.addActionListener(new ActionListener() {
                    public void actionPerformed(ActionEvent e) {
                        Tile tile = (Tile) e.getSource();
                        int r = tile.r;
                        int c = tile.c;
                        if (numSelected != null) {
                            if (tile.getText() != "") {
                                return;
                            }
                            String numSelectedText = numSelected.getText();
                            String tileSolution = String.valueOf(solution[r].charAt(c));
                            if (tileSolution.equals(numSelectedText)) {
                                tile.setText(numSelectedText);
                                tile.setBackground(Color.lightGray);
                                HighlightNumber(numSelectedText);
                                if (isComplete()) {
                                    JOptionPane.showMessageDialog(frame, "Congratulations! You solved the Sudoku!");
                                    String[][] puzzleAndSolution = SudokuGenerator.generatePuzzle();
                                    puzzle = puzzleAndSolution[0];
                                    solution = puzzleAndSolution[1];

                                    setupTiles();
                                    setupButtons();

                                    // Clear old tiles and buttons
                                    boardPanel.removeAll();
                                    buttonsPanel.removeAll();

                                    // Re-add new tiles and buttons
                                    setupTiles();
                                    setupButtons();

                                    // Refresh the panels
                                    boardPanel.revalidate();
                                    boardPanel.repaint();
                                    buttonsPanel.revalidate();
                                    buttonsPanel.repaint();
                                }
                            }
                            else {
                                errors += 1;
                                textLabel.setText("Sudoku | Errors: " + String.valueOf(errors));
                            }
                        }
                    }
                });
            }
        }

    }

    void setupButtons() {
        for (int i = 1; i < 10; i++) {
            JButton button = new JButton();
            button.setFont(new Font("Arial", Font.BOLD, 20));
            button.setText(String.valueOf(i));
            button.setFocusable(false);
            button.setBackground(Color.WHITE);
            buttonsPanel.add(button);

            button.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    JButton button = (JButton) e.getSource();
                    if (numSelected != null) {
                        numSelected.setBackground(Color.WHITE);
                    }
                    numSelected = button;
                    numSelected.setBackground(Color.lightGray);
                    HighlightNumber(button.getText());
                }
            });
        }
    }

    boolean isComplete() {
        for  (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                String tileText = ((Tile) boardPanel.getComponent(r * 9 + c)).getText();
                if (!tileText.equals(String.valueOf(solution[r].charAt(c)))) {
                    return false;
                }
            }
        }
        return true;
    }

    void HighlightNumber(String number) {
        int done = 0;
        for (int i = 0; i < 81; i++) {
            Tile tile = (Tile) boardPanel.getComponent(i);
            if (puzzle[tile.r].charAt(tile.c) != '-') {
                tile.setBackground(Color.LIGHT_GRAY);  // pre-filled
            } else if (tile.getText() != "") {
                tile.setBackground(Color.LIGHT_GRAY);
            } else {
                tile.setBackground(Color.WHITE);       // blank
            }
            if (!tile.getText().isEmpty() && tile.getText().equals(number)) {
                tile.setBackground(Color.YELLOW);
                done++;
            }
        }

        if (done == 9) {
            JButton btn = (JButton) buttonsPanel.getComponent(Integer.parseInt(number) - 1);
            btn.setBackground(Color.BLACK);
            btn.setEnabled(false);
            btn.setBackground(Color.BLACK);
        }
    }
}
