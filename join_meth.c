#include<stdio.h>
#include<stdlib.h>

int index_chr(char* c, char** chrnames, int n){
    int i;
    for(i=0; i<n; i++){

         
    }
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
    fclose(fchr);
    fprintf(stderr,"%d chromosome(s) found\n",c);
    char** chrnames;
    chrnames = (char**)malloc(c*sizeof(char*));
    int i;
    fchr=fopen(argv[1],"r");
    for( i=0; i<c; i++ ) {
        chrnames[i]=malloc(100);
        fscanf(fchr,"%s",chrnames[i]);
        fprintf(stderr,"%s\n",chrnames[i]);
    }
     

}
