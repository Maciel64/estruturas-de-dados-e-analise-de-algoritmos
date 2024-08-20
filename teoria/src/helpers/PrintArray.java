package helpers;

public class PrintArray {
  public static void print(int[] array) {
    System.out.print("[");

    for (int c = 0; c <= array.length - 1; c++) {
      if (c == array.length - 1) {
        System.out.print(array[c]);
        continue;
      }

      System.out.print(array[c] + ", ");
    }

    System.out.println("]");
  }
}
