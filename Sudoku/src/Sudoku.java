import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.net.URL;
import javax.imageio.ImageIO;
import javax.swing.*;

public class Sudoku {
    // color list

    Color notFound = Color.WHITE;
    Color found = (new Color(255, 185, 225));
    Color Correct = Color.GREEN;
    Color Out = Color.DARK_GRAY;
    Color Highlighted = (new Color(191, 223, 255));
    Color BackgroundColor = (new Color(255, 214, 237));

    public String numSelectedText = "";

    static class Tile extends JButton {
        int r;
        int c;

        Tile(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    int boardWidth = 600;
    int boardHeight = 700;

    String[][] puzzleAndSolution = SudokuGenerator.generatePuzzle();
    String[] puzzle = puzzleAndSolution[0];
    String[] solution = puzzleAndSolution[1];

    JFrame frame = new JFrame("Sudoku");
    JLabel textLabel = new JLabel();
    JPanel textPanel = new JPanel();
    JPanel boardPanel = new JPanel();
    JPanel buttonsPanel = new JPanel();

    boolean logoOn = true;

    JButton numSelected = null;
    int errors = 0;

    String text = "<html>" +
            "<span style='color:#ff80c0'>|</span>" +
            "<span style='color:white'>  Errors: <span style='color:black'>" +
            errors +
            "</span></html>";

    public Image logoImage = null;


    Sudoku() {

        try {
            BufferedImage img = ImageIO.read(getClass().getResource("/logo.png")); // logo in same folder
            Image scaled = img.getScaledInstance(200, 140, Image.SCALE_SMOOTH);

            // Circular mask
            BufferedImage circleImg = new BufferedImage(150, 100, BufferedImage.TYPE_INT_ARGB);
            Graphics2D g2 = circleImg.createGraphics();
            g2.setClip(new java.awt.geom.Ellipse2D.Float(0, 0, 150, 100));
            g2.drawImage(scaled, 0, 0, null);
            g2.dispose();

            logoImage = ImageIO.read(getClass().getResource("/icon.png")); // use for icon too

        } catch (Exception e) {
            System.out.println("Logo not found.");
        }

        if (logoImage != null) frame.setIconImage(logoImage);

        ImageIcon logo = new ImageIcon(getClass().getResource("/logo.png"));
        Image img = logo.getImage().getScaledInstance(150, 100, Image.SCALE_SMOOTH);
        logo = new ImageIcon(img);
        JLabel logoLabel = new JLabel(logo);


        textPanel.add(logoLabel);
        frame.setSize(boardWidth, boardHeight);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setLayout(new BorderLayout());

        textLabel.setFont(new Font("Arial", Font.BOLD, 30));
        textLabel.setHorizontalAlignment(JLabel.CENTER);

        textLabel.setText(text);

        textPanel.add(textLabel);
        frame.add(textPanel, BorderLayout.NORTH);

        boardPanel.setLayout(new GridLayout(9, 9));
        setupTiles();

        frame.add(boardPanel);

        buttonsPanel.setLayout(new GridLayout(1, 9));
        setupButtons();
        frame.add(buttonsPanel, BorderLayout.SOUTH);

        frame.getContentPane().setBackground(BackgroundColor);
        frame.setVisible(true);

        boardPanel.setBorder(BorderFactory.createEmptyBorder(0, 10, 10, 10));
        buttonsPanel.setBorder(BorderFactory.createEmptyBorder(5, 10, 10, 10));

        textPanel.setOpaque(false);
        buttonsPanel.setOpaque(false);
        boardPanel.setOpaque(false);

    }

    void setupTiles() {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                Tile tile = new Tile(r, c);
                char titleChar = puzzle[r].charAt(c);

                if (titleChar == '-') {
                    tile.setText("");
                    tile.setBackground(notFound);
                } else {
                    tile.setText(String.valueOf(titleChar));
                    tile.setBackground(found);
                }

                tile.setFocusable(false);

                tile.setPreferredSize(new Dimension(60, 60));
                tile.setFont(new Font("Arial", Font.BOLD, 20));
                if (r == 2 && c == 2 || r == 2 && c == 5 || r == 5 && c == 2 || r == 5 && c == 5) {
                    tile.setBorder(BorderFactory.createMatteBorder(1, 1, 5, 5, Color.BLACK));
                } else if (r == 2 || r == 5) {
                    tile.setBorder(BorderFactory.createMatteBorder(1, 1, 5, 1, Color.BLACK));
                } else if (c == 2 || c == 5) {
                    tile.setBorder(BorderFactory.createMatteBorder(1, 1, 1, 5, Color.BLACK));
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
                            numSelectedText = numSelected.getText();
                            String tileSolution = String.valueOf(solution[r].charAt(c));
                            if (tileSolution.equals(numSelectedText)) {
                                tile.setText(numSelectedText);
                                tile.setBackground(Correct);
                                new javax.swing.Timer(500, d -> {
                                    if (numSelectedText.equals(numSelected.getText()) && !numSelectedText.isEmpty()) {
                                        HighlightNumber(numSelectedText);
                                    }
                                }).start();
                                if (isComplete()) {
                                    JOptionPane.showMessageDialog(frame, "Congratulations! You solved the Sudoku!");
                                    frame.dispose();
                                    new MainMenu();
                                }
                            } else {
                                if (numSelectedText == "") {
                                    JOptionPane.showMessageDialog(frame, "Pick a new number.");
                                    return;
                                } else {
                                    errors += 1;

                                    text = "<html>" + "<span style='color:#ff80c0'>S</span>" +
                                            "                <span style='color:white'>u</span>" +
                                            "                <span style='color:grey'>d</span>" +
                                            "                <span style='color:#ff80c0'>o</span>" +
                                            "                <span style='color:white'>k</span>" +
                                            "                <span style='color:#ff80c0'>u</span>" +
                                            " |  <span style='color:white'>  Errors: <span style='color:black'>" +
                                            errors +
                                            "</span></html>";

                                    textLabel.setText(text);
                                }
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
            button.setBackground(notFound);
            buttonsPanel.add(button);

            button.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    JButton button = (JButton) e.getSource();
                    if (numSelected != null && !numSelected.getText().isEmpty()) {
                        numSelected.setBackground(notFound);
                    }
                    numSelected = button;
                    numSelected.setBackground(Highlighted);
                    HighlightNumber(button.getText());
                }
            });
        }
    }

    boolean isComplete() {
        for (int r = 0; r < 9; r++) {
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
        for (
                int i = 0;
                i < 81; i++) {
            Tile tile = (Tile) boardPanel.getComponent(i);
            if (puzzle[tile.r].charAt(tile.c) != '-') {
                tile.setBackground(found);  // pre-filled
            } else if (tile.getText() != "") {
                tile.setBackground(found);
            } else {
                tile.setBackground(notFound);       // blank
            }
            if (!tile.getText().isEmpty() && tile.getText().equals(number)) {
                tile.setBackground(Highlighted);
                done++;
            }
        }

        if (done == 9) {
            JButton btn = (JButton) buttonsPanel.getComponent(Integer.parseInt(number) - 1);
            btn.setBackground(Out);
            btn.setEnabled(false);
            btn.setBackground(Out);

            numSelected.setText("");
            numSelectedText = "";

            javax.swing.Timer q = new javax.swing.Timer(25, d -> {
                for (int i = 0; i < 81; i++) {
                    Tile tile = (Tile) boardPanel.getComponent(i);
                    if (!tile.getText().isEmpty() && tile.getText().equals(number)) {
                        tile.setBackground(Correct);
                    }
                }
            });

            q.setRepeats(false);
            q.start();

            javax.swing.Timer t = new javax.swing.Timer(500, d -> {
                for (int i = 0; i < 81; i++) {
                    Tile tile = (Tile) boardPanel.getComponent(i);
                    if (!tile.getText().isEmpty() && tile.getText().equals(number)) {
                        tile.setBackground(found);
                    }
                }
            });

            t.setRepeats(false);
            t.start();
        }
    }
}
