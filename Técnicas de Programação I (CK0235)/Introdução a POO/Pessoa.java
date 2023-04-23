class Pessoa {
  
    String nome;
    String cpf;
    String rua;
    String numero;
    int idade;
  
    Casamento meu_casamento;
  
    Pessoa () {
      setNome("SEM NOME");
      setCPF("000.000.000-00");
    }
    
    Pessoa (String nome) {
      setNome(nome);
      setCPF("000.000.000-00");
    }
  
    Pessoa (String nome, String cpf) {
      setNome(nome);
      setCPF(cpf);
    }
  
    static void mensagem () {
      System.out.println("Oi");
    }
  
    void setNome (String nome) {
      this.nome = nome;
    }
  
    String getNome () {
      return this.nome;
    }
  
    void setCPF (String cpf) {
      this.cpf = cpf;
    }
  
    String getCPF () {
      return this.cpf;
    }
  
    void setCasamento (Casamento c) {
      meu_casamento = c;
    }
  }