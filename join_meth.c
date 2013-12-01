#include<stdio.h>
#include<stdlib.h>

int index_chr(char* c, char** chrnames, int n){
    int i;
    for(i=0; i<n; i++){
        if ( strcmp( chrnames[i] , c )==0 ) {
            return i;
        }
    }
    return -1;
}


int max(int a, int b){
    if (a>b) return a; else return b;

}
int main(int argc, char* argv[]){
    if (argc<4) {
        fprintf(stderr,"usage: <chr file> <methyl1> <methyl2>\n");
        exit(1);
    }
    // read ordered list of chromosomes    
    FILE* fchr=fopen(argv[1],"r");
    char* buffer=malloc(100);
    int c  = 0;
    //count lines
    while(1){
        buffer = fgets(buffer,100,fchr);
        if ( feof( fchr ) ) break;
        c++;     
    }
    // 
    fclose(fchr);
    fprintf(stderr,"%d chromosome(s) found\n",c);
    char** chrnames;
    chrnames = ( char** ) malloc( c*sizeof(char*) );
    int i;
    fchr=fopen(argv[1],"r");
    //
    for( i=0; i<c; i++ ) {
        chrnames[i] = malloc( 100 );
        fscanf( fchr , "%s" , chrnames[i] );
        fprintf( stderr , "%s\n" , chrnames[i] );
    }
    //
    
    fclose(fchr);
    char* line1=malloc(1000);
    char* line2=malloc(1000);

    FILE* f1=fopen(argv[2],"r");
    FILE* f2=fopen(argv[3],"r");
    
    char* sep ="\\t ";
    char* word;
    char *chr1,*chr2;
    int pos1,pos2,i1,i2,mini,minpos;
    chr1=malloc(100);
    chr2=malloc(100);
    line1 = fgets( line1, 1000, f1  );
    line2 = fgets( line2, 1000, f2  );
    if ( feof(f1) || feof(f2) ) exit(0);
    sscanf( line1 , "%s %d" , chr1 , &pos1 ); 
    sscanf( line2 , "%s %d" , chr2 , &pos2 ); 
    i1 = index_chr( chr1 , chrnames , c );
    i2 = index_chr( chr2 , chrnames , c );
    maxi = max(i1,i2);
    maxpos = max(pos1,pos2);
    while(1){
        fprintf(stderr,"maxi:%d,maxpos:%d line1:%s line2:%s",
            maxi,maxpos,line1,line2);
        if ( i1 == i2 && pos1 == pos2 ) fprintf(stdout,"%s\t%s\n",line1,line2);
        if (i1 < maxi ){
            line1 = fgets( line1, 1000, f1  );
            if ( feof( f1 )  ) break;
            sscanf( line1 , "%s %d" , chr1 , &pos1 ); 
        }
        if ( i1 == maxi && pos1 < pos2 ){
             
        }
        //fprintf(stdout,"%s %d %s %d\n",chr1,pos1,chr2,pos2);
        i1 = index_chr( chr1 , chrnames , c );
        i2 = index_chr( chr2 , chrnames , c );
        //fprintf(stdout,"%d %d\n",i1,i2);
        maxi   = max(i1,i2);
        maxpos = max(pos1,pos2);
    }
}
