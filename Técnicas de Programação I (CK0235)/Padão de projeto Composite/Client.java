public class Client {
    public static void main(String[] args) {
        Expressao e1, e2, e3,e4;

        //expressão
        //  e1  e2  e3   e4
        //(2+3) - (5- (4 + 4) )

        e1 = new Operador('+', new Operando(2) , new Operando(3));
        e4 = new Operador('+', new Operando(4) , new Operando(4));
        e3 = new Operador('-', new Operando(5) ,e4);
        e2 = new Operador('-', e1, e3);

        System.out.println(e2.operation());
    }
}
