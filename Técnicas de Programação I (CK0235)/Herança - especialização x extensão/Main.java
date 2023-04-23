public class Main {
    public static void main(String[] args) {
        Base base = new Base();
        Derivada derivada = new Derivada();
        Base baseDerivada = new Derivada();

        int x = base.i;
        int y = derivada.i;
        int z = baseDerivada.i;

        String xstr = base.teste();
        String ystr = derivada.teste();
        String zstr = baseDerivada.teste();

        System.out.println("x = "+x);
        System.out.println("y = "+y);
        System.out.println("z = "+z);

        System.out.println("XSTR = "+ xstr);
        System.out.println("YSTR = "+ ystr);
        System.out.println("ZSTR = "+ zstr);
    }
}
