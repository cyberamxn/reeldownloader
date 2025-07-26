import http.client

conn = http.client.HTTPSConnection("instagram-reels-downloader-api.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "e10b993b2bmshba131c16b20e561p13b98ejsnb22c81e8351b",
    'x-rapidapi-host': "instagram-reels-downloader-api.p.rapidapi.com"
}

conn.request("GET", "/download?url=https%3A%2F%2Fwww.instagram.com%2Freel%2FDJg8Hc_zkot%2F%3Figsh%3DMXFvaDhueHozZjQ2bQ%3D%3D", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
