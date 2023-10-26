public class test {
  public static void main(String[] args) {
    int a = 4, b = 7, c = 10;
    boolean result = (a++ > 4) && (++b < 7) || (c-- > 9);
    System.out.println(result + " " + a + " " + b + " " + c);
  }
}
