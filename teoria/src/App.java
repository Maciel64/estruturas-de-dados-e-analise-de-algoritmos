import helpers.PrintArray;
import sorts.BubbleSort;

public class App {
    public static void main(String args[]) {
        var sort = new BubbleSort();
        int[] arr = {
                87, 45, 12, 33, 98, 77, 56, 23, 74, 31,
                6, 18, 92, 53, 11, 69, 28, 84, 7, 63,
                30, 15, 99, 49, 22, 60, 2, 46, 78, 40,
                21, 85, 51, 5, 88, 37, 10, 81, 66, 42,
                3, 57, 76, 26, 13, 90, 9, 70, 41, 62,
        };

        PrintArray.print(sort.sort(arr));
    }
}
