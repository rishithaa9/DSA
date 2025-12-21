//Write a program in C++ to display the sum of the series [ 9 + 99 + 999 + 9999 ...].


#include <iostream>
using namespace std;

int main(){
    int n;
    int sum=0;

    cout << "Enter the number: ";
    cin>>n;

    if(n<=0){
        cout << "Enter a postiive number";
        return 0;
    }
    for (int i=n;i=n;i){
        sum=sum+(i);
    }
    cout<< "Sum of the series: "<<sum<<endl;


}