import java.sql.*;
import java.time.LocalDate;
import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import java.io.File;
import javax.imageio.ImageIO;

public class BankAccount {

    private static final String DB_FILE = "bank_account.db";

    public static void main(String[] args) {
        createTable(); // Ensure database table exists
        SwingUtilities.invokeLater(() -> createGUI());
    }

    // --- DATABASE FUNCTIONS ---

    public static void createTable() {
        String sql = """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                description TEXT,
                amount REAL NOT NULL,
                balance REAL NOT NULL,
                category TEXT NOT NULL
            );
        """;

        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:" + DB_FILE);
             Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
        } catch (SQLException e) {
            System.out.println("Error creating table: " + e.getMessage());
        }
    }

    public static double getCurrentBalance() {
        double balance = 0;
        String sql = "SELECT balance FROM transactions ORDER BY id DESC LIMIT 1";

        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:" + DB_FILE);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            if (rs.next()) {
                balance = rs.getDouble("balance");
            }

        } catch (SQLException e) {
            System.out.println("Error getting balance: " + e.getMessage());
        }
        return balance;
    }

    public static void addTransaction(String desc, double amount, String category) {
        double currentBalance = getCurrentBalance();
        double newBalance = currentBalance + amount;

        String sql = "INSERT INTO transactions(date, description, amount, balance, category) VALUES(?, ?, ?, ?, ?)";

        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:" + DB_FILE);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, LocalDate.now().toString());
            pstmt.setString(2, desc);
            pstmt.setDouble(3, amount);
            pstmt.setDouble(4, newBalance);
            pstmt.setString(5, category);
            pstmt.executeUpdate();

        } catch (SQLException e) {
            System.out.println("Error adding transaction: " + e.getMessage());
        }
    }

    public static String getTransactionHistory() {
        StringBuilder sb = new StringBuilder();
        String sql = "SELECT date, description, amount, balance, category FROM transactions ORDER BY id ASC";

        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:" + DB_FILE);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                sb.append(String.format("%s  |  %s | %s | %+.2f | Balance: %.2f%n",
                        rs.getString("date"),
                        rs.getString("description"),
                        rs.getString("category"),
                        rs.getDouble("amount"),
                        rs.getDouble("balance")));
            }

        } catch (SQLException e) {
            System.out.println("Error getting transactions: " + e.getMessage());
        }

        return sb.toString();
    }

    // --- GUI FUNCTIONS ---
    public static void createGUI() {
        JFrame frame = new JFrame("Bank Account App");
        frame.setSize(500, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Top panel: Current balance
        // Load logo

        // GUI CONFIG

        boolean logoOn = false;


        //

        JPanel topPanel = new JPanel();

        if (logoOn == true) {
            Image logoImage = null;
            try {
                BufferedImage img = ImageIO.read(new File("logo.png")); // logo in same folder
                Image scaled = img.getScaledInstance(50, 50, Image.SCALE_SMOOTH);

                // Circular mask
                BufferedImage circleImg = new BufferedImage(50, 50, BufferedImage.TYPE_INT_ARGB);
                Graphics2D g2 = circleImg.createGraphics();
                g2.setClip(new java.awt.geom.Ellipse2D.Float(0, 0, 50, 50));
                g2.drawImage(scaled, 0, 0, null);
                g2.dispose();

                logoImage = circleImg; // use for icon too

            } catch (Exception e) {
                System.out.println("Logo not found.");
            }

            if (logoImage != null) frame.setIconImage(logoImage);

            ImageIcon logo = new ImageIcon("logo.png");
            Image img = logo.getImage().getScaledInstance(50, 50, Image.SCALE_SMOOTH);
            logo = new ImageIcon(img);
            JLabel logoLabel = new JLabel(logo);
            topPanel.add(logoLabel);
        }
            JLabel balanceLabel = new JLabel(String.format("Balance: $%.2f", getCurrentBalance()));
            balanceLabel.setFont(new Font("Verdana", Font.BOLD, 18));
            topPanel.add(balanceLabel);
            frame.add(topPanel, BorderLayout.NORTH);
            topPanel.setBackground(new Color(30, 30, 30));
            balanceLabel.setForeground(new Color(225, 225, 225));  

        
        

        // Center panel: Transaction history
        JTextArea historyArea = new JTextArea();
        historyArea.setEditable(false);
        historyArea.setFont(new Font("Verdana", Font.PLAIN, 12));
        JScrollPane scrollPane = new JScrollPane(historyArea);
        historyArea.setText(getTransactionHistory());
        frame.add(scrollPane, BorderLayout.CENTER);
        historyArea.setBackground(new Color(20, 20, 20));
        historyArea.setForeground(Color.WHITE);  


        // Bottom panel: Add transactions
        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new GridLayout(4, 2, 5, 5));

        JTextField descField = new JTextField();
        JTextField categoryField = new JTextField();
        JTextField amountField = new JTextField();

        JButton depositButton = new JButton("Deposit");

        JButton withdrawButton = new JButton("Withdraw");
        depositButton.setBackground(new Color(30, 30, 30));
        depositButton.setForeground(new Color(225, 225, 225));
        withdrawButton.setBackground(new Color(30, 30, 30));
        withdrawButton.setForeground(new Color(225, 225, 225));

        JLabel descLabel = new JLabel("Description:");
        descLabel.setForeground(Color.WHITE);  
        bottomPanel.add(descLabel);
        bottomPanel.add(descField);
        JLabel categoryLabel = new JLabel("Category:");
        categoryLabel.setForeground(Color.WHITE);  
        bottomPanel.add(categoryLabel);
        bottomPanel.add(categoryField);
        JLabel amountLabel = new JLabel("Amount:");
        amountLabel.setForeground(Color.WHITE);  
        bottomPanel.add(amountLabel);
        bottomPanel.add(amountField);
        bottomPanel.add(depositButton);
        bottomPanel.add(withdrawButton);
        bottomPanel.setBackground(new Color(25, 25, 25));
        bottomPanel.setForeground(Color.WHITE);  


        frame.add(bottomPanel, BorderLayout.SOUTH);

        // Button actions
        depositButton.addActionListener(e -> {
            String desc = descField.getText();
            String category = categoryField.getText();
            double amt;
            try {
                amt = Double.parseDouble(amountField.getText());
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Enter a valid number!");
                return;
            }
            addTransaction(desc, amt, category);
            descField.setText("");
            amountField.setText("");
            categoryField.setText("");
            balanceLabel.setText("Balance: $" + getCurrentBalance());
            historyArea.setText(getTransactionHistory());
        });

        withdrawButton.addActionListener(e -> {
            String desc = descField.getText();
            String category = categoryField.getText();
            double amt;
            try {
                amt = Double.parseDouble(amountField.getText());
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Enter a valid number!");
                return;
            }
            addTransaction(desc, -amt, category);
            descField.setText("");
            amountField.setText("");
            categoryField.setText("");
            balanceLabel.setText("Balance: $" + getCurrentBalance());
            historyArea.setText(getTransactionHistory());
        });

        frame.setVisible(true);
    }
}
