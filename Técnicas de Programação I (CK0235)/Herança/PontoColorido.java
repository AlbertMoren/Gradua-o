public class PontoColorido extends Ponto{
    int cor;
    
    //Construtor da classe Ponto colorido
    PontoColorido(float x1, float y1, int cor){
        super(x1, y1); //chama o construtor da classe Ponto
        this.cor = cor;
    }

    void setCor(int cor){
        this.cor = cor;
    }

    int getCor(){
        return cor;
    }
}
