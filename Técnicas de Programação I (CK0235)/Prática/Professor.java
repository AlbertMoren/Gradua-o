public class Professor extends Pessoa{
    private Disciplina disciplina;

    Professor(String nome,String sexo, int idade){
        super(nome,sexo,idade);
    }

    public void setDisciplina(Disciplina disciplina) {
        this.disciplina = disciplina;
    }

    public Disciplina getDisciplina() {
        return disciplina;
    }

    @Override
    public String toString() {
        return "Professor [nome=" + nome + ", genero=" + sexo + ", idade=" + idade + ", Disciplina=" + disciplina + "]";
    }
    
}
