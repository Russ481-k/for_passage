package app;
public class OopBasics {
  public static class Animal { public String speak(){ return "..." ; } }
  public static class Dog extends Animal { @Override public String speak(){ return "woof"; } }
  public static String who(Animal a){ return a.speak(); }
}
