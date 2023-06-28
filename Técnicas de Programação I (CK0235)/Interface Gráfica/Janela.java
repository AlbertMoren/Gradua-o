import java.awt.*;


public class Janela{
   
    //Conteiner frame
    public Janela(){
       Frame f = new Frame("Titulo");
        f.setSize(200, 200);
        f.setBackground(Color.red);
        f.setResizable(true);
        f.setVisible(true);

        //Associar o trador de eventos com a janela
        Tratador tratar = new Tratador();
        f.addWindowListener(tratar);

        //Definindo Layout Maneger
        //f.setLayout(null);

        //Conteiner Panel
        Panel p = new Panel();
        p.setBackground(Color.blue);
        Panel p1 = new Panel();
        p1.setBackground(Color.red);
        Panel p2 = new Panel();
        p2.setBackground(Color.red);
        Panel p3 = new Panel();
        p3.setBackground(Color.red);
    
        //Componentes
        Label l = new Label("Meu label",Label.CENTER);
        l.setBounds(100, 100, 160,20);
        l.setCursor(new Cursor(Cursor.HAND_CURSOR));
        Label l2 = new Label("Outro label",Label.CENTER);

        Button b = new Button("ok");
        b.addActionListener(tratar);
        b.setBounds(150, 150,150,50);
        // Adicionando componentes ao conteiner Panel
        p.add(l);
        p.add(b);
        f.add("Center",p);
        f.add("North",p1);
        f.add("South",p2);
        f.add("East",p3);
        f.add("West",l2);

        f.pack();
    
    }


}

