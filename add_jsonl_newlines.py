from datetime import date
import json


def main():
    file_name = 'honeies_list.jsonl'
    date_today = date.today().strftime("%Y%m%d")
    write_file_name = f"honeies_list_{date_today}.jsonl"
    # create (touch) write_file_elements file
    with open(write_file_name, 'w') as file:
        pass
    file.close()

    print(f"Creating a new file: {write_file_name}")
    print(f"type of write_file_name: {type(write_file_name)}")

    new_lines_num = 10

    write_file_elements = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            write_file_elements = list(map(lambda x: json.loads(x.strip()), lines.copy()))
            last_element = lines[len(lines) - 1]
            print (f"Last element in the file: {last_element}")
            last_json = json.loads(last_element)
            print(f"Last JSON object: {last_json}")
            last_id = last_json.get("id", None)
            sample_jsonl = """{"id":310,"name":"","beekeeper":"","prefecture":"","city":"","country":"japan","flowers":[],"year":0,"expired_at_year":0,"expired_at_month":0,"bouhgt_in":""}"""
            sample_json = json.loads(sample_jsonl)
            for i in range(new_lines_num):
                last_id = last_id + 1
                sample_json["id"] = last_id
                print(f"New JSON object to be added: {sample_json}")
                write_file_elements.append({
        "id": last_id,
        "name": "",
        "beekeeper": "",
        "prefecture": "",
        "city": "",
        "country": "japan",
        "flowers": [],
        "year": 0,
        "expired_at_year": 0,
        "expired_at_month": 0,
        "bouhgt_in": ""
    })
            file.close()
        print(f"write_file_name : {write_file_name}")

        with open(write_file_name, 'w', encoding='utf-8') as file:
            for element in write_file_elements:
                file.write(json.dumps(element, ensure_ascii=False) + "\n")
            file.close()


    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return
    
    print(f"Reading from file: {file_name}")
    print(f"Writing to file: {write_file_name}")


if __name__ == "__main__":
    main()
    