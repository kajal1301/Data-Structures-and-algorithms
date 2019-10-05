public class LcsDp{
    public static int max(int a,int b){
        mx=a>b?a:b;
        return mx;
    }
    public static int Lcs(String p, String q, int m,int n){
        int result[][]= new int[n+1][m+1];
        for(int i=0; i<=n;i++){
            for(int j=0; j<=m; j++){
                if(i==0|| j==0)
                    result[i][j]=0;
                else if(p.charAt(i-1)== q.charAt(j-1)){
                    result[i][j]= 1+ result[i-1][j-1];
                }
                else
                    result[i][j]= max(result[i-1][j],result[i][j-1]);
                }
            }
            return result[n][m];
        }
        public static void main(String[] args){
           String p="kajal";
           String q= "anchal";
           int m=5;
           int n=6;        
           int x= Lcs(p,q,m,n);
            System.out.println(x);
        }


    }
