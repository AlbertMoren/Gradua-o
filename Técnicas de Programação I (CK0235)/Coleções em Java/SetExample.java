import java.util.HashSet;

import java.util.*;
public class SetExample {
    public static void main(String[] args) {
        Set set = new HashSet<>();
        
        set.add("one");
        set.add("seconde");
        set.add("3rd");
        set.add(new Integer(4));
        set.add(new Float(5.04f));
        set.add("seconde");
        set.add(new Integer(4));
        System.out.println(set);
        
    }
    
}