import json

def read_text_file(file_path: str) -> str:
    return open(file_path).read()

def read_jsonl_line_by_line(contents: str) -> list[str]:
    lines = contents.splitlines()
    output = []
    for line in lines:
        current_line_json = json.loads(line)  # This will raise an error if the line is not valid JSON  
        beekeeper = current_line_json.get("beekeeper", "Unknown Beekeeper")
        print(current_line_json.get("id", "No ID found"))
        if not beekeeper:
            print("No beekeeper information found in this line.")
            continue
        else:
            print(f"Beekeeper: {beekeeper}")
            output.append(beekeeper)
    print(f"Total beekeepers found: {len(output)}")
    return output

def write_beekeeper_line_by_line(beekeepers: list[str], file_path: str):
    with open(file_path, "w") as f:
        for beekeeper in beekeepers:
            f.write(beekeeper + "\n")
    f.close()

def main():
    file_path = "honeies_list.jsonl"
    try:
        content = read_text_file(file_path)
        print("File content:")
        bks = read_jsonl_line_by_line(content)
        bk_set = set(bks)  # Remove duplicates
        write_beekeeper_line_by_line(bk_set, "beekeeper_list.csv")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
