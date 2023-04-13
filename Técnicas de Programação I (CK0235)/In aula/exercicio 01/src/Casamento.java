public class Casamento {
    Pessoa p1,p2;
    Boolean valido = true;

    Casamento(Feminino p1,Masculino p2){
        this(p2,p1);
    }

    Casamento(Masculino p1, Feminino p2){
        this.p1 = p1;
        this.p2 = p2;
        if(validar()){
            this.p1.setCasamento(this);
            this.p2.setCasamento(this);
        }else{
            this.valido = false;
        }
    }

    Boolean validar(){
        if (p1 == p2){
            return false;
        }
        if(p1.getIdade() <18 || p2.getIdade() < 18){
            return false;
        }
        if(p1.getCasamento() != null || p2.getCasamento() != null)
            return false;
        return true;
    }
}
