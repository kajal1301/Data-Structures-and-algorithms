public class RodCut{
    public static int max(int q, int a){
        if(q>a)
        return q;
        else
         return a;
    }
    public static int CutRod(int[] p, int n){
        int q;
        if(n==0){
            return 0;
        }
        else{
            q= -1;
            for(int i=1; i<n;i++){
                q= max(q, p[i]+CutRod(p, n-1));
            }
        }
        return q;
    }
    public static void main(String[] args){
         int [] p= {2,4,6,8,9};
         System.out.println("maximum profit is:"+ CutRod(p,5));
    }
}