class Main {
    public static void main (String args[]){
  
      Pessoa p1, p2 ;
      Casamento c;
  
      p1 = new Pessoa ("JOE");
      Pessoa.mensagem();
  
      p2 = new Pessoa ("Mary");
      
  
      c = new Casamento();
  
      //c.marido = p1;
      //c.mulher = p1;
  
       if (!c.casar(p1,p1))         
          System.out.println ("Erro: nao casaram");
          else { 
            Pessoa p3 = c.getMulher();
            p3.setNome("xxx");
            System.out.println(c.getMulher().getNome());
          }
  
  
  
    }
  }