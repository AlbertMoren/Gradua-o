public class Main {
    public static void main(String[] args) throws Exception {
        Pessoa p1, p2;

        p1 = new Feminino("Ana", 21);
        p2 = new Masculino("Tiago", 22);
        Casamento casamento = new Casamento(p1, p2);
    }
}
