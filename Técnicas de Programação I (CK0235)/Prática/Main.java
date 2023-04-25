public class Main {
    public static void main(String[] args) {
        Escola escola = new Escola();

        // criar alguns alunos
        Aluno aluno1 = new Aluno("João", "M", 18, 1234);
        Aluno aluno2 = new Aluno("Maria", "F", 19, 5678);

        // matricular os alunos na escola
        escola.matriculaAluno(aluno1);
        escola.matriculaAluno(aluno2);

        // criar alguns professores
        Professor professor1 = new Professor("José", "M", 35);
        Professor professor2 = new Professor("Ana", "F", 28);

        // contratar os professores pela escola
        escola.contratarProfessor(professor1);
        escola.contratarProfessor(professor2);

        // criar algumas disciplinas
        DisciplinaPratica disciplina1 = new DisciplinaPratica("Física", 60, "Laboratório A");
        DisciplinaTeorica disciplina2 = new DisciplinaTeorica("Matemática", 80, "Álgebra Linear");

        // adicionar as disciplinas na escola
        escola.adicionarDisciplina(disciplina1);
        escola.adicionarDisciplina(disciplina2);

        // alocar disciplinas para professores
        escola.alocarDisciplina(professor1, disciplina1);
        escola.alocarDisciplina(professor2, disciplina2);

        // imprimir lista de alunos, professores e disciplinas
        System.out.println("Lista de alunos:");
        escola.listaAlunos();

        System.out.println("Lista de professores:");
        escola.listaProfessor();

        System.out.println("Lista de disciplinas:");
        escola.listaDisciplina();
    }
}
