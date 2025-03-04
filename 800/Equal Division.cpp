#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int ts;
    cin>>ts;
    while(ts--){
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
        cin>>arr[i];
        
        if(n==1)
            cout<<"YES"<<endl;
        else{
            int extra=0,sum_of_all=0;
            for(int i=0;i<n;i++)
                sum_of_all+=arr[i];

            int exact=sum_of_all/n;
            for(int i=0;i<n;i++){
                if(arr[i]<exact){
                    int need=exact-arr[i];
                    arr[i]=arr[i]+min(need,extra);
                    extra=extra-need;
                    if(arr[i]<exact){
                    cout<<"NO"<<endl;
                    break;}
                }

                else{
                    extra=extra+(arr[i]-exact);
                    arr[i]=exact;
                    
                }
            }
            if(extra==0)
            cout<<"YES"<<endl;
        }
        }
        return 0;
    }