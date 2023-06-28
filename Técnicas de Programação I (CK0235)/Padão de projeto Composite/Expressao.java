//Composite
public abstract class Expressao{
    abstract float operation();
    abstract void add(Expressao e);
    abstract void remove(Expressao e);
    abstract void getChild();
}