import pandas as pd
import json

excel_file = '/Users/anishkumar/PycharmProjects/PythonProjects/practice_python/Tests/S_test/test.xlsx'
df = pd.read_excel(excel_file,sheet_name= 'Sheet1')
# print(df)
value = df.iloc[0,0]

print(value)

def validate_int(x) :
    try :
        x = int(x)
    except ValueError :
        print(f'Not a valid id: {x}')
    else :
        return x


def validate_string(x) :
    try :
        x = str(x)
    except ValueError :
        print(f'Not a valid String: {x}')
    else :
        return x


def validate_ppu(ppu) :
    ppu = validate_int(ppu)
    if ppu and (ppu < 1 and ppu > 0) :
        return ppu
    else :
        print(f"NOT a valid PPU {ppu}")
    return None


def validate_topping_id(topping_id) :
    topping_id = validate_int(topping_id)
    if topping_id and topping_id in (5001, 5002, 5003, 5004, 5005, 5006, 5007) :
        return topping_id
    else :
        print(f"NOT a valid topping id {topping_id}")
    return None



cell_string = value  #
try :
    data = json.loads(cell_string)
except ValueError :
    print("Not a valid json")

for entry in data :
    if 'id' in entry :
        validate_int(entry['id'])
    else :
        print("ID not found")

    if 'type' in entry :
        validate_string(entry['type'])
    else :
        print("type not found")

    if 'name' in entry :
        validate_string(entry['name'])
    else :
        print("name not found")

    if 'ppu' in entry :
        validate_ppu(entry['ppu'])
    else :
        print("ppu not found")

    if not 'batters' in entry :
        print("batters not found")

    if 'topping' in entry :
        for topping_entry in entry['topping'] :
            if 'id' in topping_entry :
                validate_topping_id(topping_entry['id'])
            else :
                print("Topping ID not found")
            # validate type
            if 'type' in topping_entry :
                validate_string(topping_entry['type'])
            else :
                print("topping type not found")
    else :
        print("topping not found")


