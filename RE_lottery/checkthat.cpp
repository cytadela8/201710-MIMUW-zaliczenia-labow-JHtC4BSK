#include <iostream>
#include <random>

using namespace std;

int main() {
	std::mt19937 gen1(0);
	std::mt19937 gen2(0);
	std::uniform_int_distribution<> dis(0, 255);
	cout << gen1() << " " << gen1()  << " " << gen1()  << " " << gen1()  << " " << gen1()  << " " << gen1()  << " " << gen1()  << " " << gen1()  << " " << gen1()  << "\n";
        cout << gen2() << " " << gen2() << " " << dis(gen2) << " " << gen2() << " " << dis(gen2)  << " " << dis(gen2) << " " << dis(gen2) << " " << gen2() << "\n\n";
	{
	std::mt19937 gen1(0);
	std::mt19937 gen2(0);
	std::uniform_int_distribution<> dis(0, 255);
	for (int i=0;i<100;i++)
		cout << gen1()/(1<<(32-8)) << " ";
	cout << "\n";
	for (int i=0;i<100;i++)
		cout << dis(gen2) << " ";
	}
}
