#include <iostream>
#include <fstream>

void victory() {
    std::fstream flag_input("flag.txt", std::fstream::in);
    std::string flag;

    flag_input >> flag;

    std::cout << flag << std::endl;
}

void foo() {
    uint8_t c, tab[30];
    volatile auto ptr = &victory;
    size_t i = 0;

    std::cout << "victory is nearby: " << std::hex <<
     reinterpret_cast<uint64_t>(&foo) << " like " <<
     (reinterpret_cast<int64_t>(&victory) - reinterpret_cast<int64_t>(&foo)) << std::endl;

    //for (int i=0;i<8;i++)
    //	std::cout << std::hex << (int)tab[i] << " ";

    while(std::cin >> c) {
        tab[i++] ^= c;
    }
    if(*reinterpret_cast<uint64_t*>(tab) == reinterpret_cast<uint64_t>(ptr)) {
        victory();
    }
}

int main() {
    foo();
}
