//finallap to riches and I don't how to code this to cheapest phones for Old times childhood dream job loss safety to go back up the ladder or have an adventure at high speed with an unbreakable device for 1 week charge
import javax.microedition.midlet.*;
import javax.microedition.lcdui.*;
import java.util.Random;


//made with gemini not tested on real phone this is for 10$ phones..


public class RandomStringMIDlet extends MIDlet implements CommandListener {
    private Display display;
    private Form mainForm;
    private StringItem resultItem;
    private Command exitCommand;
    private Command generateCommand;
    
    // Your list of strings
    private String[] options = {"left", "right", "up", "down"};
    private Random random = new Random();

    public RandomStringMIDlet() {
        display = Display.getDisplay(this);
        mainForm = new Form("Randomizer");
        resultItem = new StringItem("Result: ", "Press Gen");
        
        exitCommand = new Command("Exit", Command.EXIT, 0);
        generateCommand = new Command("Generate", Command.SCREEN, 1);
        
        mainForm.append(resultItem);
        mainForm.addCommand(exitCommand);
        mainForm.addCommand(generateCommand);
        mainForm.setCommandListener(this);
    }

    public void startApp() {
        display.setCurrent(mainForm);
    }

    public void pauseApp() {}

    public void destroyApp(boolean unconditional) {}

    public void commandAction(Command c, Displayable s) {
        if (c == exitCommand) {
            notifyDestroyed();
        } else if (c == generateCommand) {
            // Logic to pick a random index
            int index = random.nextInt(options.length);
            resultItem.setText(options[index]);
        }
    }
}
