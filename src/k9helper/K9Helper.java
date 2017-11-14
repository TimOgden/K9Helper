/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package k9helper;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Tim
 */
public class K9Helper {

    private static ArrayList<Quote> quotes;
    private static long timeToWait = 12000;
    private static long timeStarted = 0;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException, IOException {
        // TODO code application logic here
        Scanner scan = new Scanner(new File("info.txt"));
        GUI gui = null;

        if (!scan.hasNext()) {
            PasswordGiver passwordGiver = new PasswordGiver();
            String password = createPassword(16);
            BufferedWriter writer = new BufferedWriter(new FileWriter("info.txt"));
            writer.write(encrypt(password));
            writer.close();
            passwordGiver.getjTextArea1().setText("Here is your password. Don't write it down anywhere, this app will store it for you. Just run it again to see it:\n" + password);
            passwordGiver.setVisible(true);
        } else {
            gui = new GUI();
            gui.getjTextArea1().setLineWrap(true);
            loadQuotes();
            timeStarted = System.currentTimeMillis();
            Random randQuote = new Random();
            Quote q = quotes.get(randQuote.nextInt(quotes.size()));
            gui.getjTextArea1().setText("\"" + q.getQuote() + "\"\n\t-" + q.getSpeaker());
            gui.getjProgressBar1().setMinimum((int) timeStarted);
            gui.getjProgressBar1().setMaximum((int) (timeStarted + timeToWait));
            gui.setVisible(true);
        }
        if (gui != null) {
            int i = 1;
            while (System.currentTimeMillis() - timeStarted < timeToWait) {
                gui.getjProgressBar1().setValue((int) System.currentTimeMillis());
                if ((System.currentTimeMillis() - timeStarted) / 10000 >= i) {
                    Random randQuote = new Random();
                    Quote q = quotes.get(randQuote.nextInt(quotes.size()));
                    gui.getjTextArea1().setText("\"" + q.getQuote() + "\"\n\t-" + q.getSpeaker());
                    i++;
                    
                }
            }
            Scanner read = new Scanner(new File("info.txt"));
            gui.getjTextArea1().setText("Thank you for waiting. Your password is:\n\t" + decrypt(read.nextLine()));
            
        }
    }

    private static String createPassword(int length) {
        String SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        StringBuilder salt = new StringBuilder();
        Random rnd = new Random();
        while (salt.length() < length) { // length of the random string.
            int index = (int) (rnd.nextFloat() * SALTCHARS.length());
            salt.append(SALTCHARS.charAt(index));
        }
        String saltStr = salt.toString();
        return saltStr;

    }

    private static String encrypt(String password) {
        String s = "";
        char[] temp = password.toCharArray();
        for (int i = 0; i < temp.length; i++) {
            s += (char) (temp[i] + 2);
        }
        return s;
    }

    private static String decrypt(String password) {
        String s = "";
        char[] temp = password.toCharArray();
        for (int i = 0; i < temp.length; i++) {
            s += (char) (temp[i] - 2);
        }
        return s;
    }
    
    private static void loadQuotes() throws FileNotFoundException {
        if (quotes == null) {
            quotes = new ArrayList<>();
        }
        Scanner scan = new Scanner(new File("quotes.txt"));
        String first = "", second = "";
        int i = 0;
        while (scan.hasNextLine()) {
            if (i % 2 == 0) {
                first = scan.nextLine();
            }
            if (i % 2 != 0) {
                second = scan.nextLine();
                quotes.add(new Quote(first, second));
            }
            i++;
        }

    }
}
