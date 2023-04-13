abstract class Pessoa {
    private String nome;
    private int idade;
    //private char sexo;
    private Casamento casamento;
    
    public Casamento getCasamento() {
        return casamento;
    }
    public void setCasamento(Casamento casamento) {
        this.casamento = casamento;
    }
    Pessoa(){
        this("Sem nome",0);
    }

    Pessoa (String nome){
        this(nome,0);
    }

    Pessoa(String nome, int idade){
        this.setNome(nome);
        this.setIdade(idade);
        //this.setSexo(sexo);
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    /*public void setSexo(char sexo) {
        this.sexo = sexo;
    }*/

    public String getNome() {
        return nome;
    }
    public int getIdade() {
        return idade;
    }
    /*public char getSexo() {
        return sexo;
    }*/
}
