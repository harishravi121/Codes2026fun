Creating a maze-solving application with a manual "step-by-step" button requires a combination of **Swing** (for the UI) and a **Flood Fill** variant (typically Breadth-First Search or Depth-First Search) to track the path.

In this implementation, the "Glow" effect is achieved by changing the cell color as the algorithm progresses.

### Java Implementation: Maze Flood Fill

This code creates a $10 \times 10$ grid. You can click cells to toggle walls (black) and use the "Next Step" button to see the flood fill spread (cyan).

```java
import javax.swing.*;
import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;

public class MazeApp extends JFrame {
    private final int SIZE = 10;
    private JButton[][] cells = new JButton[SIZE][SIZE];
    private int[][] maze = new int[SIZE][SIZE]; // 0: empty, 1: wall, 2: visited
    private Queue<Point> queue = new LinkedList<>();
    
    public MazeApp() {
        setTitle("Maze Flood Fill - Step by Step");
        setSize(600, 700);
        setLayout(new BorderLayout());

        JPanel gridPanel = new JPanel(new GridLayout(SIZE, SIZE));
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                cells[r][c] = new JButton();
                cells[r][c].setBackground(Color.WHITE);
                int row = r, col = c;
                cells[r][c].addActionListener(e -> toggleWall(row, col));
                gridPanel.add(cells[r][c]);
            }
        }

        JButton nextButton = new JButton("Next Step (Flood Fill)");
        nextButton.addActionListener(e -> performFloodFillStep());

        // Start point
        queue.add(new Point(0, 0));
        cells[0][0].setText("START");

        add(gridPanel, BorderLayout.CENTER);
        add(nextButton, BorderLayout.SOUTH);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    private void toggleWall(int r, int c) {
        if (maze[r][c] == 0) {
            maze[r][c] = 1;
            cells[r][c].setBackground(Color.BLACK);
        } else {
            maze[r][c] = 0;
            cells[r][c].setBackground(Color.WHITE);
        }
    }

    private void performFloodFillStep() {
        if (queue.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Fill Complete or No Path!");
            return;
        }

        int size = queue.size();
        for (int i = 0; i < size; i++) {
            Point p = queue.poll();
            int r = p.x;
            int c = p.y;

            // Directions: Up, Down, Left, Right
            int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < SIZE && nc >= 0 && nc < SIZE && maze[nr][nc] == 0) {
                    maze[nr][nc] = 2; // Mark as visited
                    cells[nr][nc].setBackground(Color.CYAN); // "Glow" effect
                    queue.add(new Point(nr, nc));
                }
            }
        }
    }

    public static void main(String[] args) {
        new MazeApp();
    }
}

```

---

### How the Algorithm Works

The Flood Fill algorithm is essentially a **Breadth-First Search (BFS)** when applied to a grid for pathfinding.

1. **Queue Initialization:** We start by pushing the starting coordinates $(x, y)$ into a queue.
2. **The "Turn" (Button Click):** Every time you click the button, the app processes the current "layer" of the queue.
3. **Expansion:** For every point in the queue, it checks the neighbors (North, South, East, West).
4. **The Glow:** If a neighbor is a valid path (not a wall and not already visited), it changes the color to **Cyan** (the glow) and adds it to the queue for the next turn.

### Mathematical Logic

The distance $d$ from the start can be represented as:


$$d(P_1, P_2) = |x_1 - x_2| + |y_1 - y_2|$$


This is known as **Manhattan Distance**, which the flood fill follows as it expands layer by layer through the maze grid.

Would you like me to add a "target" coordinate so the algorithm stops automatically once it finds the exit?
