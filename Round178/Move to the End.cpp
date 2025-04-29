#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int z;
    cin >> z;
    while (z--) {
        int n;
        cin >> n;
        vector<long long> v(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i];
        }

        reverse(v.begin(), v.end());
        vector<long long> suf_max(n);
        suf_max[n-1] = v[n-1];
        for (int i = n-2; i >= 0; i--) {
            suf_max[i] = max(v[i], suf_max[i+1]);
        }

        long long sum_v = 0;
        for (int i = 0; i < n; i++) {
            cout << sum_v + suf_max[i] << " ";  
            sum_v += v[i];  
            
        }
        cout << endl;
    }
    return 0;
}