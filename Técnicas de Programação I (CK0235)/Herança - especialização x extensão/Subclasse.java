public class Subclasse extends Super{
    Subclasse(){
        //super();
        System.out.println("Construtor Subclasse");
    }
    
    void teste(){
        super.teste();
        System.out.println("Metodo subclasse");
    }
}