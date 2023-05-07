public class Main {
    public static void main(String[] args) {
        Escalavel e;

        e = new CirculoEscalavel();
    
        System.out.println(e instanceof ObjetoGeometrico);
        System.out.println(e instanceof Escalavel);
        System.out.println(e instanceof Circulo);
        System.out.println(e instanceof CirculoEscalavel);
      
    }
}
