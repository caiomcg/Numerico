#include <stdio.h>

void questao01_e(int n, double a[n][n], double b[n], double U[n][n], double L[n][n], double x[n], double y[n]){
    int i, j, k;
    double mult;
    for(i=1; i<=n-1; i++){
        for(j=0; j<=i-1; j++){
            mult = U[i][j]/U[j][j];
            L[i][j] = (mult); //Insere os multiplicadores na matriz L
            printf("L%d = L%d - %lf*L%d\n", i+1, i+1, mult, i);
            for(k=0; k<n; k++){
                U[i][k] -= (mult*U[k][k]); //Altera os valores da matriz U
                printf("U[%d][%d] = U[%d][%d] - %lf*U[%d][%d] = %lf\n", i+1, k+1, i+1, k+1, mult, k+1, k+1, U[i][k]);

            }
        }
    }

    //Faz LY = B
    for(i=0; i<n; i++){
        //j só vai até i porque acima da diagonal principal há apenas zeros na matriz L
        y[i] = b[i];
        for(j=0; j<i; j++){
            y[i] -= L[i][j]*y[j];
        }
    }

    //Faz UX = B
    //i Inicializa em n-1 por ser a última linha, que é onde precisa-se apenas de 1 operação para encontrar o X
    for(i=n-1; i>=0; i--){
        //j só vai até i porque abaixo da diagonal principal há apenas zeros
        x[i] = b[i];
        for(j=n-1; j>=i; j--){
            x[i] -= L[i][j]*x[j];
        }
    }
}

int main(){
    const int n = 3;
    int i, j;
    double a[3][3] = {{5,1,-2},{3,-9.4,1.8},{1,2.2,4.6}}; //Inicializa a matriz a
    double b[3] = {10,22,10}, //inicializa o vetor b
           U[n][n], //Cria a matriz U
           L[3][3] = {{0}}, //Preenche a matriz L com 0s
           x[n], y[n];

    for(i=0; i<n; i++)
        L[i][i] = 1; //Preenche a diagonal da matriz L com 1s

    for(i=0; i<n; i++)
        for(j=0; j<n; j++)
            U[i][j] = a[i][j]; //Copia a matriz a para a U

    questao01_e(n, a, b, U, L, x, y);

    printf("\n----------U----------\n");
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            printf("%lf ", U[i][j]);
        }
        printf("\n");
    }

    printf("\n----------L----------\n");
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            printf("%lf ", L[i][j]);
        }
        printf("\n");
    }

    printf("\n----------x----------\n");
    for(i=0; i<n; i++){
        printf("%lf\n", x[i]);
    }

    printf("\n----------y----------\n");
    for(i=0; i<n; i++){
        printf("%lf\n", y[i]);
    }

    return 0;
}
