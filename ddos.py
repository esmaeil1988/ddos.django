import requests
u="http://127.0.0.1:8000/contact/?nam=%D8%A7%D8%B3%D9%85%D8%A7%D8%B9%DB%8C%D9%84+%D8%B1%D9%81%DB%8C%D8%B9%DB%8C&email=me%40gmail.com&onvan=ddos&matn=ddos"
for i in range(100):
    requests.get(url=u)