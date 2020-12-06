#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <vector>


using li = long int;
using ll = long long;


int two_sum(std::vector<ll> &arr, size_t left, int target){
    std::size_t right = arr.size() - 1;

    int cur;
    while (left < right)
    {
        cur = arr.at(left) + arr.at(right);
        if (cur < target)
            ++left;
        else if (cur > target)
            --right;
        else
            return arr.at(left) * arr.at(right);
    }
    return -1;
}


int three_sum(std::vector<ll> &arr, int target){
    using std::size_t;
    for (size_t idx{ 0 }; idx < arr.size(); ++idx)
    {
        int two_res{ two_sum(arr, idx + 1, target - arr[idx]) };
        if (two_res > 0)
            return arr[idx] * two_res;
    }
    return -1;
}


int main(){
    using std::cout;
	std::vector<ll> arr( std::istream_iterator<long int>(std::cin), {});
    std::sort(arr.begin(), arr.end());
    cout << "Res a: " << two_sum(arr, 0, 2020) << "\n";
    cout << "Res b: " << three_sum(arr, 2020) << "\n";
    return 0;
}