#include <stdio.h>
void mularr(int *arr1,int *arr2,int size,int *result) {
    for (int i =0;i<size;i++) {
        for (int j=0;j<size;j++) {
            result[i+j*size]=arr1[i]*arr2[j];
        }
    }
}
int main() {
    int arr1[9] = {1,2,3,4,5,6,7,8,9};
    int arr2[9] = {9,8,7,6,5,4,3,2,1};
    int result[81];
    mularr(arr1,arr2,9,result);
    for (int i = 0; i < 81; i++) {
        printf("%4d ", result[i]); // 4칸 확보해서 출력
        if ((i + 1) % 9 == 0) printf("\n"); // 10개마다 줄바꿈
    }
}