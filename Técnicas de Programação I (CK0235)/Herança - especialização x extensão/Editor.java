class Editor {
  // COM CONCEITO DE CLASSE ABSTRATA
  Figura listaFig[] = new Figura[100];

  void criarFigura (Figura f) {
    listaFig[iFig] = r;
    iFig++;   
  }

 void interfaceGUI () {
    Figura f;
    if (click == "Ret") f = new Retangulo();
    if (click == "Circ") f = new Circulo();     
    if (click == "Tri") f = new Triangulo();
    //if (click == "Eli") f = new Elipse();
    criarFigura(f);
  }

  void desenharTodasFiguras () {
     for (int i=0, i < iFig; i++) {
      listaFig[iFig].desenhar();
    }
  }   



  // SEM CONCEITO DE CLASSE ABSTRATA

  int iRet, iCirc, iTri;
  Retangulo listaRet [] = new Retangulo[100];
  Circulo ListaCirc[] = new Circulo[100];
  Triangulo ListaTriangulo[] = new Triangulo[100];

  void criarRetangulo (Retangulo r) {
    listaRet[iRet] = r;
    iRet++;
  }

  void criarCirculo (Circulo c) {
    listaRet[iCirc] = c;
    iCirc++;
  }

  void criarTriangulo (Triangulo t) {
    listaRet[iTri] = t;
    iTri++;
  }

  void desenharTodasFiguras () {
    for (int i=0, i < iRet; i++) {
      listaRet[iRet].desenhar();
    }

     for (int i=0, i < iCirc; i++) {
      listaCirc[iCirc].desenhar();
    }

     for (int i=0, i < iTri; i++) {
      listaTri[iTri].desenhar();
    }
  }

  void interfaceGUI () {
    if (click == "Ret") this.criarRetangulo(new Retangulo());
    
    if (click == "Circ") this.criarCirculo(new Circulo()); 
        
    if (click == "Tri") this.criarTriangulo(new Triangulo()); 
  }

}