package app;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class OopBasicsTest {
  @Test void dogShouldSpeak(){
    assertEquals("woof", new OopBasics.Dog().speak());
  }
  @Test void polymorphism(){
    OopBasics.Animal a = new OopBasics.Dog();
    assertEquals("woof", OopBasics.who(a));
  }
}
