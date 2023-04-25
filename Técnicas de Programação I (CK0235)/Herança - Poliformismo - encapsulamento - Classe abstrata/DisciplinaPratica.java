public class DisciplinaPratica extends Disciplina{
    private String local;

    DisciplinaPratica(String nome,int carga,String local){
        super(nome,carga);
        this.local = local;
    }

    public String getLocal() {
        return local;
    }

    public void setLocal(String local) {
        this.local = local;
    }
    
}
