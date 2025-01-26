import java.util.Random;

public class SingingLyrics {
    // ANSI escape codes for colors
    private static final String[] COLORS = {
        "\u001B[31m", // Red
        "\u001B[32m", // Green
        "\u001B[33m", // Yellow
        "\u001B[34m", // Blue
        "\u001B[35m", // Magenta
        "\u001B[36m", // Cyan
        "\u001B[37m"  // White
    };

    private static final String RESET_COLOR = "\u001B[0m"; // Reset to default color

    // Lyrics for karaoke-style display
    private static final String[] LYRICS = {
        "Alam mo bang pang-malupitang banat ko?",
        "Hindi ka na dito belong",
        "Tanginamo 'pag kami nangyamot sa'yo, dapat hindi ka pikon",
        "Pa'no mo nasabi na hindi ko kaya makipagsabayan",
        "Sa mga ganito patayan, kayang-kaya ko tapakan ang pangalan mo",
        "Putangina mo, ngayon, sino sa'tin ang magaling?"
    };

    public static void main(String[] args) {
        Thread soundBarsThread = new Thread(() -> {
            try {
                runSoundBars();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread lyricsThread = new Thread(() -> {
            try {
                runLyrics();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        // Start both threads
        soundBarsThread.start();
        lyricsThread.start();
    }

    private static void runSoundBars() throws InterruptedException {
        Random random = new Random();
        int numBars = 10;   // Number of sound bars
        int maxHeight = 10; // Max height for the sound bars

        while (true) {
            // Generate random heights for each bar
            int[] barHeights = new int[numBars];
            for (int i = 0; i < numBars; i++) {
                barHeights[i] = random.nextInt(maxHeight) + 1;
            }

            // Clear the screen
            System.out.print("\033[H\033[2J");
            System.out.flush();

            // Draw the sound bars
            drawSoundBars(barHeights, maxHeight);

            // Shorter delay for smooth sound bar animation
            Thread.sleep(200); // Adjust for faster/slower animation
        }
    }

    private static void runLyrics() throws InterruptedException {
        int lyricIndex = 0;

        while (true) {
            // Display the current lyric at the bottom
            if (lyricIndex < LYRICS.length) {
                System.out.println("\n\n" + RESET_COLOR + LYRICS[lyricIndex]); // Print the current lyric
                lyricIndex++; // Move to the next lyric
            } else {
                lyricIndex = 0; // Loop back to the start of the lyrics
            }

            // Longer delay for lyric changes
            Thread.sleep(11500); // Adjust for faster/slower lyric timing
        }
    }

    private static void drawSoundBars(int[] barHeights, int maxHeight) {
        int numBars = barHeights.length;

        // Draw the bars row by row (from top to bottom)
        for (int row = maxHeight; row > 0; row--) {
            for (int col = 0; col < numBars; col++) {
                String color = COLORS[col % COLORS.length]; // Cycle through colors
                if (barHeights[col] >= row) {
                    System.out.print(color + "█ " + RESET_COLOR); // Bar block
                } else {
                    System.out.print("  "); // Empty space
                }
            }
            System.out.println(); // Move to the next row
        }
    }
}
