#include <stdio.h>

void print_arr(int *arr,int size) {
    for (int i=0;i<size;i++) {
        printf("%d ",arr[i]);
    }
    printf("\n");
}
int *rotate(int * arr,int size,int rotate) {
    for (int j =0;j<rotate;j++) {
        int temp = arr[size-1];
        for (int i = size-1;i>0;i--) {
            arr[i] = arr[i-1];
        }
        arr[1] = arr[0];
        arr[0] = temp;
    }
    return arr;
}
int main() {
    int arr[6] = {1,2,3,4,5,6};
    print_arr(arr,6);
    int * newarr = rotate(arr,6,6);
    print_arr(newarr,6);
}
