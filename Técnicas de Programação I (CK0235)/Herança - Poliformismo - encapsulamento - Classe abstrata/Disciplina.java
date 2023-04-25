public abstract class Disciplina {
    private String nome;
    private int cargaHoraria;

    Disciplina(String nome,int carga){
        this.nome = nome;
        this.cargaHoraria = carga;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getCargaHoraria() {
        return cargaHoraria;
    }

    public void setCargaHoraria(int cargaHoraria) {
        this.cargaHoraria = cargaHoraria;
    }

    public String toString() {
        return "Disciplona [ nome = "+ nome + " Carga Horaria = " + cargaHoraria + "]";
    }

}
