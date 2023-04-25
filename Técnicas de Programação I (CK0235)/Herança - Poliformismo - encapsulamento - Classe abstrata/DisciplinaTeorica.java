public class DisciplinaTeorica extends Disciplina{
    private String conteudo;

    DisciplinaTeorica(String nome,int carga,String conteudo){
        super(nome,carga);
        this.conteudo = conteudo;
    }

    public String getConteudo() {
        return conteudo;
    }

    public void setConteudo(String conteudo) {
        this.conteudo = conteudo;
    }
    
}
