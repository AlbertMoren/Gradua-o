import java.awt.*;

public class BorderLayoutExample{
   public static void main(String[] args) {
		// Instancia um novo frame.
		// BorderLayout é o "default".
		Frame frame = new Frame();
		Button button;
		// Instancia um novo botão.
		button = new Button("Norte");
		// Configura a fonte do botão.
		button.setFont(new Font("Arial", Font.PLAIN, 20));
		// Adiciona o botão ao "frame".
		frame.add("North",button);
        button = new Button("Sul");
		button.setFont(new Font("Arial", Font.BOLD, 20));
		frame.add("South",button);
		button = new Button("Leste");
		button.setFont(new Font("Arial", Font.ITALIC, 20));
		frame.add("East", button);

		button = new Button("Oeste");
		button.setFont(new Font("Arial", Font.PLAIN, 20));
		frame.add("West", button);
        button = new Button("Centro");
		button.setFont(new Font("Arial", Font.ITALIC|Font.BOLD, 20));
		frame.add("Center", button);

		frame.pack();
		frame.setVisible(true);
   }
}
