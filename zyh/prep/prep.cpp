#include "json/json.h"
#include "json/value.h"
#include "json/reader.h"
#include "json/writer.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void PrepJson()
{
    
	Json::Reader reader;
	Json::Value rootin;
	Json::Value rootout;
    int i = 0;

	ifstream in("Data/TestData/2020-01-01-0.json", ios::binary);
	if (!in.is_open())
	{
		cout << "Error opening file\n";
		return;
	}
    ofstream os;
	os.open("Data/TestData/Prepared_Test_Data.json", std::ios::out | std::ios::app);
	if (!os.is_open())
    {
        cout << "error：can not find or create the file which named \" Wdemo.json\"." << endl;
        return;
    }

    string str;
    while(getline(in, str))
    {
        if (reader.parse(str, rootin))
	    {
            i ++;
            rootout["id"] = rootin["id"];
            rootout["type"] = rootin["type"];
            rootout["actor"]["id"] = rootin["actor"]["id"];
            rootout["actor"]["login"] = rootin["actor"]["login"];
            rootout["actor"]["display_login"] = rootin["actor"]["diaplay_login"];
            rootout["actor"]["gravator_id"] = rootin["actor"]["gravator_id"];
            rootout["actor"]["url"] = rootin["actor"]["url"];
            rootout["actor"]["avator_url"] = rootin["actor"]["avator_url"];
            rootout["repo"]["id"] = rootin["repo"]["id"];
            rootout["repo"]["name"] = rootin["repo"]["name"];
            rootout["repo"]["url"] = rootin["repo"]["url"];
            rootout["public"] = rootin["public"];
            rootout["created_at"] = rootin["created_at"];

	        Json::StyledWriter sw;
	        os << sw.write(rootout) << endl;
	    }
        else
        {
            cout << "FORMAT ERR" << endl;
        }
    }
    in.close();
    os.close();

    cout << i << endl;
}

int main () {
    PrepJson();
    return 0;
}