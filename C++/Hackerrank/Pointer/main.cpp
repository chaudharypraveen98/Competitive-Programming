#include <iostream>

void sumAndAbsDiff(int* a, int* b) {
    int tmpA = *a;
    // a' -> |a+b|
    *a += *b;
    // b' -> a - b
    *b -= tmpA;
    // |b'|
    *b = std::abs(*b);
}

int main() {
    int a = 0;
    int b = 0;
    
    std::cin >> a >> b;
    
    sumAndAbsDiff(&a, &b);
    
    std::cout << a << std::endl << b;
    
    return 0;
}