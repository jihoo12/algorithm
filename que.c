#include <stdio.h>

void print_arr(int *arr,int size) {
    for (int i=0;i<size;i++) {
        printf("%d ",arr[i]);
    }
    printf("\n");
}
int main() {
    int arr[5] = {1,2,3,4,5};
    print_arr(arr,5);
}