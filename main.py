import requests

def main():
    res = requests.get("https://www.yahoo.co.jp/")
    print(res.status_code)
    print("Hello from study-uv!")


if __name__ == "__main__":
    main()
