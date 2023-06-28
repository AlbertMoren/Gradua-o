import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

class Tratador implements WindowListener, ActionListener{

    @Override
    public void windowClosing(WindowEvent e) {
        System.exit(0);
    }
    
    @Override
    public void windowActivated(WindowEvent e) {
        System.out.println("Activede");
    }

    @Override
    public void windowClosed(WindowEvent e) {
        System.out.println("Closed");
    }

    @Override
    public void windowDeactivated(WindowEvent e) {
        System.out.println("Deactivated");
    }

    @Override
    public void windowDeiconified(WindowEvent e) {
        System.out.println("Deiconifield");
    }

    @Override
    public void windowIconified(WindowEvent e) {
        System.out.println("Iconified");
    }

    @Override
    public void windowOpened(WindowEvent e) {
        System.out.println("Opened");
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Cliquei");
    }

    
    
}
