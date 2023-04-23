class Casamento {
    private Pessoa marido, mulher;
    //Date data_casamento;
    int anos_casados;
  
    boolean casar (Pessoa marido, Pessoa mulher) {
      if (marido != mulher) {
        this.marido = marido;
        this.mulher = mulher;
        marido.setCasamento(this);
        mulher.setCasamento(this);
      } else {
        return false;
      }
      return true;
    }
  
    Pessoa getMarido () {
      return this.marido;
    }
  
    Pessoa getMulher () {
      return this.mulher;
    }
  }