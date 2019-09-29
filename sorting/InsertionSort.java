import java.util.Scanner;
public class InsertionSort{
    public static int[] InsertSort(int[] arr, int n){
        for(int j=2; j<n; j++){
            int key= arr[j];
            int i= j-1;
            while(i>0 && arr[i]>key){
                arr[i+1]= arr[i];
                i--;
                arr[i+1]= key;
            }   
             }
             return arr;
     }
     public static void main(String[] args){
        
        System.out.println("Enter the size of array:");
        Scanner sc= new Scanner(System.in);
        int n= sc.nextInt();
        int[] arr= new int[n];
        System.out.println("Enter the elements of array:");
        for(int i=0; i<n;i++){
            arr[i]= sc.nextInt();
        }
        InsertSort(arr, n-1);
        for(int i=0;i<n;i++){
            System.out.println(arr[i]);
        }
     }
}