#include <iostream>

struct Student {
    int age;
    int standard;
    
    std::string first_name;
    std::string last_name;
};

int main() {
    Student st;
    
    std::cin >> st.age >> st.first_name >> st.last_name >> st.standard;
    std::cout << st.age << " " << st.first_name << " " << st.last_name << " " << st.standard;
    
    return 0;
}