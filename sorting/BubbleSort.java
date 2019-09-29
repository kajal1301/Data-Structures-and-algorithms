import java.util.Scanner;
public class BubbleSort{
    public static int[] Bubble_Sort(int [] arr, int n){
        for(int j=0; j<n; j++){
            for(int i=0; i< n-j; i++){
                if(arr[i+1]< arr[i]){
                    int m= arr[i+1];
                    arr[i+1]= arr[i];
                    arr[i]= m;
                }
            }
        }
        return arr;
    }
    public static void main(String [] args){
        System.out.println("Enter the size of array:");
        Scanner sc= new Scanner(System.in);
        int n= sc.nextInt();
        int[] arr= new int[n];
        System.out.println("Enter the elements of array:");
        for(int i=0; i<n;i++){
            arr[i]= sc.nextInt();
        }
        Bubble_Sort(arr, n-1);
        for(int i=0;i<n;i++){
            System.out.println(arr[i]);
        }
     }
}