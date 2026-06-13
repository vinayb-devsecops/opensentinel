import json

def load_trends():

    with open("trends/cve_history.json","r") as f:
        return json.load(f)

if __name__ == "__main__":
    print(load_trends())
