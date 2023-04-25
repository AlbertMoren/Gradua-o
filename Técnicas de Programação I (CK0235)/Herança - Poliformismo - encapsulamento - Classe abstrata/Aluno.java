public class Aluno extends Pessoa {

    private int matricula;

    Aluno(String nome,String sexo, int idade,int matricula){
        super(nome,sexo,idade);
        this.matricula = matricula;
    }

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    
    public String toString() {
        return "Aluno [nome=" + nome + ", genero=" + sexo + ", idade=" + idade + ", matricula=" + matricula + "]";
    }
    
}
