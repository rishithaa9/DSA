#include <stdio.h>
int n;
int main() {
    int find,res;
    printf("Enter the number of elements in array: ");
    scanf("%d",&n);

    int arr[n];
    for (int i=0;i<n;i++) {
        prinf("Enter the element at index %d ",i);
        scanf("%d",&arr[i]);
    }

    printf("Enter the element to find in the array: ");
    scanf("%d",&find);

    res = binarySearch_recursion(arr,find);

    return 0;
}
int binarySearch_recursion(arr,elem) {
    int temp, flag;
    for (int i=0;i<n;i++) {
        flag = 0;
        for (int j=0;j<n;j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                flag = 1;
            }
        }
        if (flag == 0)
            break;
    }

    int check=0;

}