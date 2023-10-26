import java.util.*;

public class test {

  public static void main(String[] args) {
    Scanner console = new Scanner(System.in);
    System.out.print("What is your favorite color? ");
    String name = console.next();
    if (name.equals("blue")) {
      System.out.println("Mine, too!");
    }
  }
}
