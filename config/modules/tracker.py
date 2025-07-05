import requests

def track_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'fail':
            print("❌ Invalid IP address.")
            return
        print(f"📌 IP Info for: {ip}")
        print(f"🌍 Country: {response['country']} ({response['countryCode']})")
        print(f"🏙️ City: {response['city']}")
        print(f"⏰ Timezone: {response['timezone']}")
        print(f"📶 ISP: {response['isp']}")
        print(f"🏢 Org: {response['org']}")
        print(f"📡 Latitude: {response['lat']}, Longitude: {response['lon']}")
    except:
        print("❌ Failed to fetch data.")

if __name__ == "__main__":
    ip = input("🔎 Enter IP to track: ")
    track_ip(ip)
