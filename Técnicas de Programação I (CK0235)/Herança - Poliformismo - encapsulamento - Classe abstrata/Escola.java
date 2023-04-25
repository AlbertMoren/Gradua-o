import java.util.ArrayList;
import java.util.List;

public class Escola {
    //Lista de disciplina
    private List<Aluno> aluno;
    private List<Professor> professor;
    private List<Disciplina> disciplina;

    Escola(){
        this.aluno = new ArrayList<>();
        this.professor = new ArrayList<>();
        this.disciplina = new ArrayList<>();
    }

    public void matriculaAluno(Aluno aluno){
        this.aluno.add(aluno);
    }

    public void contratarProfessor(Professor professor){
        this.professor.add(professor);
    }

    public void adicionarDisciplina(Disciplina disciplina){
        this.disciplina.add(disciplina);
    }

    public void alocarDisciplina(Professor professor, Disciplina disciplina){
        professor.setDisciplina(disciplina);
    }

    public void listaAlunos(){
        for(Aluno alunos : aluno){
            System.out.println(alunos);
        }
    }

    public void listaProfessor(){
        for(Professor professors : professor){
            System.out.println(professors);
        }
    }

    public void listaDisciplina(){
        for(Disciplina disciplinas : disciplina){
            System.out.println(disciplinas);
        }
    }
    
}
