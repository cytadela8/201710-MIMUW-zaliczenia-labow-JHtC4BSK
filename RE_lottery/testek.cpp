#include <iostream>
#include <random>

using namespace std;

int main() {
	int64_t n;
	int m;
	cin >> n >> m;
	n=4294967296;
	int wej[m];
	for (int i=0;i<m;i++)
		cin >> hex >> wej[i];
	std::mt19937 gen(0);
	std::uniform_int_distribution<> dis(0, 255);
	for (int64_t i=0;i<n;i++)
	{
		gen.seed(int32_t(i));
		bool ok = true;
		{
			for (int j=0;j<m;j++)
			{
				int val = dis(gen);
				//cout << val << "=" << wej[j];
				if(val != wej[j])
				{
					//cout << "neq";
					ok = false;
					break;
				}		
			}
		}
		if (ok)
			cout << "ZNALAZLEM!!!" << i;
	}
}
