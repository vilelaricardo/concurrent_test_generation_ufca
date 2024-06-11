import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;

public class HelperClass {
    public static int processIndex(int processId, int iteration) {
        int label = (processId / iteration);
        if (processId % iteration > 0) {
            label++;
        }
        return label;
    }

    public static boolean thisProcessIsLast(int processId, int iteration, int numberOfProcesses) {
        boolean lastProcess = false;
        int value = (numberOfProcesses / iteration + (numberOfProcesses % iteration > 0 ? 1 : 0)) - 1;
        if (processId / iteration == value) {
            lastProcess = true;
        }
        return lastProcess;
    }

    public static String makeMessagePrimes(StringBuilder builder, int value) {
        builder.append(" ").append(value);
        String address = builder.toString();
        return address;
    }

    public static String makeAddress(String ip, int port) {
        StringBuilder builder = new StringBuilder();
        builder.append(ip).append(":").append(port);
        String address = builder.toString();
        return address;
    }

    public static void makeAddressFile(int processId, String address) throws IOException {
        FileWriter ownFile = new FileWriter("parallel_sieve_" + processId + ".txt");
        PrintWriter writeFile = new PrintWriter(ownFile);
        writeFile.printf(address);
        ownFile.close();
    }

    public static void waitMaster() {
        while (!Files.exists(Paths.get("parallel_sieve_0.txt")));
    }

    public static void waitSlaves(int k) {
        for (int i = 1; i < k; i++) {
            while (!Files.exists(Paths.get("slave" + i)));
        }
    }

    public static String readRemoteIP(int processId) throws IOException {
        FileReader file = new FileReader("parallel_sieve_" + processId + ".txt");
        BufferedReader br = new BufferedReader(file);
        String fileContent;
        while ((fileContent = br.readLine()) == null) {}
        String[] remoteAddress = new String(fileContent).split(":");
        String hostIP = remoteAddress[0];
        file.close();
        return hostIP;
    }

    public static int readRemotePort(int processId) throws IOException {
        FileReader file = new FileReader("parallel_sieve_" + processId + ".txt");
        BufferedReader br = new BufferedReader(file);
        String fileContent;
        while ((fileContent = br.readLine()) == null) {}
        String[] remoteAddress = new String(fileContent).split(":");
        int remotePort = Integer.parseInt(remoteAddress[1]);
        file.close();
        return remotePort;
    }

    public static void closeFiles(int numberOfProcesses) {
        for (int i = 1; i < numberOfProcesses; i++) {
            new File("parallel_sieve_" + i + ".txt").delete();
            new File("slave" + i).delete();
        }
        new File("parallel_sieve_0.txt").delete();
    }
}