    #include <iostream>

    using namespace std;

    int main(){
        int N;
        int size;
        cin >> N;

        for (int i = 0; i < N; i++)
        {
            cin >> size;
            int arr[size];
            int flag = 0;
            for (int j = 0; j < size; j++)
            {
                cin >> arr[j];
            }

            for (int j = 0; j < size; j++)
            {
                if(j==0 && (arr[j] > arr[j+1]) ){
                    cout << j<< " ";
                    flag = 1;
                }else if(j==size-1 && (arr[j] > arr[j-1])){
                    cout << j<< " ";
                    flag = 1;
                }else if(j!=0 && j!=size-1){
                    if(arr[j] > arr[j-1] && arr[j] > arr[j+1]){
                        cout << j<< " ";
                        flag = 1;
                    }
                }
                
            }
            if (flag == 0){
                    cout << -1 << " ";
                }
            cout << endl;
            
        }
        

    }