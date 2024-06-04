import java.io.*;
import java.net.*;
import truco_java.*;

public class TrucoServer {
    private ServerSocket serverSocket;

    public TrucoServer(int port) throws IOException {
        serverSocket = new ServerSocket(port);
    }

    public void start() {
        while (true) {
            try {
                new ClientHandler(serverSocket.accept()).start();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static class ClientHandler extends Thread {
        private Socket clientSocket;
        private PrintWriter out;
        private BufferedReader in;
        private TrucoGame game;

        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
            this.game = new TrucoGame();
        }

        public void run() {
            try {
                out = new PrintWriter(clientSocket.getOutputStream(), true);
                in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                String inputLine;

                while ((inputLine = in.readLine()) != null) {
                    String response = handleCommand(inputLine);
                    out.println(response);
                }
                in.close();
                out.close();
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        private String handleCommand(String command) {
            // Aquí debes manejar los comandos, como jugar una carta, aceptar una apuesta, etc.
            // Este es un ejemplo simple que debes expandir.
            if (command.equals("state")) {
                return game.getState();  // Supongamos que TrucoGame tiene un método getState()
            } else if (command.startsWith("play")) {
                String[] parts = command.split(" ");
                int playerId = Integer.parseInt(parts[1]);
                String card = parts[2];
                return game.playCard(playerId, card);  // Supongamos que TrucoGame tiene un método playCard()
            }
            return "unknown command";
        }
    }

    public static void main(String[] args) {
        int port = 6666;  // Puerto para el servidor
        try {
            TrucoServer server = new TrucoServer(port);
            server.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
