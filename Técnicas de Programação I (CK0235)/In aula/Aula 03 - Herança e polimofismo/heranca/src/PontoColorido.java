public class PontoColorido extends Ponto{
    int cor;
    
    //Construtor da classe Ponto colorido
    PontoColorido(float x1, float y1, int c){
        super(x1, y1); //chama o construtor da classe Ponto
        cor = c;
    }

    void setCor(int c){
        cor = c;
    }

    int getCor(){
        return cor;
    }
}
