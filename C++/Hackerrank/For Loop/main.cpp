#include <iostream>
#include <string>

void printNumberDescription(int a, int b) {
    // Array of strings for English names of numbers from 1 to 9
    const std::string numberWords[] = {
        "zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine"
    };

    // We go through all the numbers from a to b inclusive
    for (int n = a; n <= b; ++n) {
        if (n >= 1 && n <= 9) {
            std::cout << numberWords[n] << std::endl;
        } else if (n > 9 && n % 2 == 0) {
            std::cout << "even" << std::endl;
        } else {
            std::cout << "odd" << std::endl; 
        }
    }
}

int main() {
    int a;
    int b;
    std::cin >> a >> b;
    printNumberDescription(a, b);
    return 0;
}