import requests

def is_hosted_by_cloudflare(url):
    try:
        response = requests.head(url, allow_redirects=True)
        server_header = response.headers.get("Server", "").lower()
        
        if "cloudflare" in server_header:
            print(f"The website {url} is hosted by Cloudflare.")
        else:
            print(f"The website {url} is NOT hosted by Cloudflare.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the website URL (including https:// or http://): ")
    is_hosted_by_cloudflare(url)
