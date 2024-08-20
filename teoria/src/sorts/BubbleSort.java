package sorts;

/**
 * Aula dia 20/08/2024 da professora Edjane
 */

public class BubbleSort {
  public int[] sort(int[] array) {
    int aux, count = 0;
    var initial = System.currentTimeMillis();

    for (int i = array.length - 1; i > 0; i--) {
      for (int k = 0; k < array.length - 1; k++) {
        if (array[k] > array[k + 1]) {
          aux = array[k];
          array[k] = array[k + 1];
          array[k + 1] = aux;
        }

        count++;
      }
    }

    var end = System.currentTimeMillis();

    System.err.printf("Demorei %dms para rodar.\n", (end - initial));
    System.out.println("Rodei " + count + " vezes");

    return array;
  }
}