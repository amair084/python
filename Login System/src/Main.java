import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        JFrame mainFrame = new JFrame();
        mainFrame.setTitle("Login Panel");
        mainFrame.setSize(750, 500);
        mainFrame.setResizable(false);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        try {
            BufferedImage logo = ImageIO.read(new File("labibi.png"));
            mainFrame.setIconImage(logo);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Load the background image
        BufferedImage bgImage = null;
        try {
            bgImage = ImageIO.read(new File("labubu.jpg")); // your background image
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Custom JPanel to draw the background image
        BufferedImage finalBgImage = bgImage; // needs to be effectively final for inner class
        JPanel backgroundPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                if (finalBgImage != null) {
                    g.drawImage(finalBgImage, 0, 0, getWidth(), getHeight(), this);
                }
            }
        };

        backgroundPanel.setLayout(null); // allows absolute positioning of components
        mainFrame.setContentPane(backgroundPanel);

        // Example: add a button on top of the background
         // Labels
        JLabel userLabel = new JLabel("Username:");
        userLabel.setForeground(Color.BLACK); // text color
        userLabel.setBounds(200, 150, 100, 25);
        backgroundPanel.add(userLabel);

        JLabel passLabel = new JLabel("Password:");
        passLabel.setForeground(Color.BLACK);
        passLabel.setBounds(200, 200, 100, 25);
        backgroundPanel.add(passLabel);

        // Text fields
        JTextField usernameField = new JTextField();
        usernameField.setBounds(300, 150, 180, 30);
        backgroundPanel.add(usernameField);

        JPasswordField passwordField = new JPasswordField();
        passwordField.setBounds(300, 200, 180, 30);
        backgroundPanel.add(passwordField);

        // Login button
        JButton loginButton = new JButton("Login");
        loginButton.setBackground(Color.WHITE);
        loginButton.setBounds(300, 250, 100, 30);
        backgroundPanel.add(loginButton);


        mainFrame.setVisible(true);

        // GUI buttons actions

        loginButton.addActionListener(e -> {
            String username = usernameField.getText();
            String password = new String(passwordField.getPassword());

            if (username.equals("labubu") && password.equals("labubu")) {

            // Reuse the already loaded background image
            BufferedImage frameBg = null;
            try {
                frameBg = ImageIO.read(new File("labubu.jpg"));
            } catch (IOException ex) {
                ex.printStackTrace();
            }

            for (int i = 1; i <= 200; i++) {
                Random rand = new Random();
                int frameWidth = 100 + rand.nextInt(400); // 200 to 599 px
                int frameHeight = 50 + rand.nextInt(300); // 150 to 449 px
                JFrame newFrame = new JFrame();
                newFrame.setTitle("Congratulations");
                newFrame.setSize(frameWidth, frameHeight);
                newFrame.setResizable(false);
                newFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

                // Random position
                int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
                int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
                int x = rand.nextInt(screenWidth - newFrame.getWidth());
                int y = rand.nextInt(screenHeight - newFrame.getHeight());
                newFrame.setLocation(x, y);

                // Custom panel for background
                BufferedImage finalFrameBg = frameBg; // effectively final
                JPanel panel = new JPanel() {
                    @Override
                    protected void paintComponent(Graphics g) {
                        super.paintComponent(g);
                        if (finalFrameBg != null) {
                            g.drawImage(finalFrameBg, 0, 0, getWidth(), getHeight(), this);
                        }
                    }
                };

        panel.setLayout(null); // optional if you want to add components
        newFrame.setContentPane(panel);
        newFrame.setVisible(true);
    }
} else {
    System.out.println("sad");
}
        });
    }
}
