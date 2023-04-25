import java.util.*;
public class ListExample {
    public static void main(String[] args) {
        List list = new ArrayList<>();
        list.add("one");
        list.add("seconde");
        list.add("3rd");
        list.add(new Integer(4));
        list.add(new Float(5.04f));
        list.add("seconde");
        list.add(new Integer(4));
        
        Iterator elements = list.iterator();
        while (elements.hasNext()){
            System.out.println(elements.next());
            elements.remove();
        }
        System.out.println(list);
    }
    
}
