#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double lngamma(const double xx) {
    int j;
    double x,tmp,y,ser,tmp2; 
    static double a[101];
    int n = (int)xx;
    if (n<=100 && a[n]>0) return a[n]; 
    static const double cof[14]={57.1562356658629235,-59.5979603554754912,
    14.1360979747417471,-0.491913816097620199,
    .339946499848118887e-4, .465236289270485756e-4,
    -.983744753048795646e-4,.158088703224912494e-3,
    -.210264441724104883e-3,.217439618115212643e-3,
    -.164318106536763890e-3, .844182239838527433e-4,
    -.261908384015814087e-4,.368991826595316234e-5}; 
    y=x=xx; 
    tmp = x+5.24218750000000000;	
    tmp = (x+0.5)*log(tmp)-tmp; 
    ser = 0.999999999999997092; 
    for (j=0;j<14;j++) ser += cof[j]/++y; 
    tmp2 = tmp + log( 2.5066282746310005*ser/x );
    if (n<=100) a[n]=tmp2;
    return tmp2 ;
}

double lnfact( int n ){
    static double a [101];
    if ( n>100 ) return lngamma( n + 1.0 );
    if ( a[n]>0 )  return a[n];
    a[n] = lngamma(n + 1.0 );
    return a[n]; 
}

double ln_beta_function(int alpha, int beta){
    return lngamma(alpha)+lngamma(beta)-lngamma(alpha+beta);
}

double h(int a1, int b1, int a2, int b2){
    double tmp;
    tmp = ln_beta_function((a1+a2),(b1+b2)) -
        ln_beta_function(a1,b1) -
        ln_beta_function(a2,b2);
    return exp(tmp);    
}

double g (int a1, int b1, int a2, int b2){
   if (a1 == b1 && b1==a2 && a2==b2) return 0.5;
   if  (a1 > 1)  {
      return  g( (a1-1), b1, a2, b2 ) + 
            h ((a1 - 1), b1, a2, b2) / ( a1 - 1 );  
    }
    if  (b1 > 1) {
        return  g (a1 ,(b1-1) ,a2, b2 ) - 
            h (a1 ,(b1-1) ,a2, b2) /  ( b1 - 1 ) ;
    }
    if  (a2 > 1) {   
        return g (a1, b1, (a2-1), b2 ) - 
            h (a1, b1, (a2-1), b2 ) /  ( a2 - 1 ) ;
    }
    if  (b2 > 1) {
       return  g( a1, b1, a2, ( b2 - 1 ) ) + 
            h (a1, b1, a2, ( b2 - 1 ) ) /   ( b2 - 1 ); 
    }
    return -1.0 ;
}



int main(){
    int nc1,c1,nc2,c2;
    int s;
    while(1){
        s=fscanf(stdin, "%d %d %d %d",&nc1,&c1,&nc2,&c2 );
        if (feof(stdin)) break;
        if (s!=4) {
            fprintf(stderr,"invalid input line\n");
            exit(1);
        }
        fprintf(stdout,"%g\n",g(nc1 + 1 , c1 + 1 , nc2 + 1 , c2 + 1 ) );
    }
    return 0;
}

