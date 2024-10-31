#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

int main() {
    int n = 0;
    std::cin >> n;
    std::vector<int> v(n);
    
    //Input vector
    for (int i = 0; i < n; ++i) {
        std::cin >> v.at(i);
    }
    
    std::sort(v.begin(), v.end());
    
    //Print vector
    std::copy(v.begin(), v.end(), std::ostream_iterator<int>(std::cout, " "));
    
    return 0;
}