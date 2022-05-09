import json
import print_me_first

def create_my_contact():
    my_contact = {"01":
                      {"firstName":"John", "lastName":"Smith", "DOB":"1/20/1991",
                       "phoneNum":{"number":"510-600-5400", "type":"cell"},
                       "address":{"street":"100 main street","city":"Fremont", "state": "CA","zipcode":"94536"}
                       },
                  "02":
                      {"firstName": "Ron", "lastName": "Robertson", "DOB": "5/23/1991",
                       "phoneNum": {"number": "510-600-8800", "type": "cell"},
                       "address":{"street":"4600 Ohlone Way","city":"Fremont", "state": "CA","zipcode":"94539"}
                       },
                  "03":
                      {"firstName": "Paul", "lastName": "Washington", "DOB": "6/15/1995",
                       "phoneNum": {"number": "510-688-1241", "type": "cell"},
                       "address": {"street": "8543 Ohlone Plaza", "city": "Fremont", "state": "CA", "zipcode": "94539"}
                       }
                  }
    return(my_contact)

def save_json_file(filename, json_object):
    with open(filename,"w") as outfile:
        outfile.write(json_object)
    outfile.close()

def open_json_file(filename):
    with open(filename,"r") as jsonfile:
        datafile = json.load(jsonfile)
        return datafile

def find_my_contact_key(key,json_data):
    print("*** Searching for ", key)
    flag = False
    for items in json_data:
        for entry in json_data[items]:
            if key == json_data[items][entry]:
                print("*** %5s" %key, "found" "    ***")
                name = json_data[items]["firstName"] + " " +json_data[items]["lastName"]
                birthday = json_data[items]["DOB"]
                cell = json_data[items]["phoneNum"]["number"]
                street = json_data[items]["address"]["street"]
                city = json_data[items]["address"]["city"]
                state = json_data[items]["address"]["state"]
                zipcode = json_data[items]["address"]["zipcode"]
                print("Name: %20s" % (name))
                print("Birthday: %12s" %(birthday))
                print("cell: %19s" %(cell))
                print("Address: %19s \n %19s, %s %s \n" %(street, city, state, zipcode))
                flag = True
            else:
                continue
    if not flag:
        any = " "
        print("*** %3s" %key, "not found" "  ***")

if __name__ == "__main__":
    print_me_first.print_me_time()
    contact = create_my_contact()
    jsonwrite = json.dumps(contact, indent=2)
    save_json_file("my_contact.json", jsonwrite)
    json_data = open_json_file("my_contact.json")
    print("***BEGiNNING OF JSON List: \n", json_data,  \
          "\n*** END OF JSON LIST\n\n")
    find_my_contact_key("Ron", json_data)
    find_my_contact_key("Sha", json_data)



