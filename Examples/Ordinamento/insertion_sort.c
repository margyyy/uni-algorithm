#include <stdio.h>

#define MAX 5

void insertionSort(int array[MAX])
{
    for (int i = 1; i < MAX; i++) {
        int key = array[i];
        int j = i - 1;
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = key;
    }
}

int main(void)
{
    int array[MAX] = {5, 4, 54, 1, 45};
    printf("Prima: ");
    for (int i = 0; i < MAX; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    insertionSort(array);
    printf("Dopo:  ");
    for (int i = 0; i < MAX; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    return 0;
}
