import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.net.URL;

public class MainMenu {
    JFrame frame = new JFrame("Hello Kitty Sudoku - Main Menu");
    public static boolean Mode = false;

    public static boolean GetMode() {
        return Mode;
    }

    public MainMenu() {
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setLayout(new BorderLayout());

        JPanel topPanel = new JPanel(new BorderLayout());
        topPanel.setBackground(new Color(255, 214, 237));

        try {
            // Load logo and icon from resources
            BufferedImage logoImg = ImageIO.read(getClass().getResource("/logo.png"));
            BufferedImage iconImg = ImageIO.read(getClass().getResource("/icon.png"));

            // Set frame icon
            if (iconImg != null) {
                frame.setIconImage(iconImg);
            }

            // Scale logo
            Image scaledLogo = logoImg.getScaledInstance(260, 190, Image.SCALE_SMOOTH);

            // Apply circular mask
            BufferedImage circleLogo = new BufferedImage(260, 190, BufferedImage.TYPE_INT_ARGB);
            Graphics2D g2 = circleLogo.createGraphics();
            g2.setClip(new java.awt.geom.Ellipse2D.Float(0, 0, 260, 190));
            g2.drawImage(scaledLogo, 0, 0, null);
            g2.dispose();

            // Add logo to JLabel
            JLabel logoLabel = new JLabel(new ImageIcon(circleLogo));
            logoLabel.setHorizontalAlignment(JLabel.CENTER);
            topPanel.add(logoLabel, BorderLayout.CENTER);

        } catch (Exception e) {
            System.out.println("Logo or icon not found: " + e.getMessage());
        }

        frame.add(topPanel, BorderLayout.NORTH);

        // -------------------- BUTTONS PANEL --------------------
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.setBackground(new Color(255, 214, 237));

        JButton startBtn = new JButton("Start Game");
        JButton easyBtn = new JButton("Normal Mode");
        JButton hardBtn = new JButton("Hard Mode");
        JButton exitBtn = new JButton("Exit");

        // Mode coloring
        if (Mode) {
            easyBtn.setBackground(Color.WHITE);
            hardBtn.setBackground(Color.LIGHT_GRAY);
        } else {
            easyBtn.setBackground(Color.LIGHT_GRAY);
            hardBtn.setBackground(Color.WHITE);
        }

        easyBtn.addActionListener(e -> {
            Mode = false;
            easyBtn.setBackground(Color.LIGHT_GRAY);
            hardBtn.setBackground(Color.WHITE);
        });

        hardBtn.addActionListener(e -> {
            Mode = true;
            easyBtn.setBackground(Color.WHITE);
            hardBtn.setBackground(Color.LIGHT_GRAY);
        });

        startBtn.setBackground(Color.WHITE);
        exitBtn.setBackground(Color.WHITE);

        startBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        easyBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        hardBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        exitBtn.setAlignmentX(Component.CENTER_ALIGNMENT);

        JPanel modePanel = new JPanel();
        modePanel.setBackground(new Color(255, 214, 237));
        modePanel.add(easyBtn);
        modePanel.add(hardBtn);

        panel.add(startBtn);
        panel.add(Box.createVerticalStrut(20));
        panel.add(modePanel);
        panel.add(Box.createVerticalStrut(20));
        panel.add(exitBtn);

        JPanel wrapper = new JPanel(new FlowLayout(FlowLayout.CENTER));
        wrapper.setBackground(new Color(255, 214, 237));
        wrapper.add(panel);

        frame.add(wrapper, BorderLayout.CENTER);

        // -------------------- BUTTON ACTIONS --------------------
        startBtn.addActionListener(e -> {
            frame.dispose();
            new Sudoku(); // launch your game
        });

        exitBtn.addActionListener(e -> System.exit(0));

        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new MainMenu();
    }
}
