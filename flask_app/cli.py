from requests import get, post, put

pk = post('http://localhost:8080/resume', json={'name': 'n1', 'title': '1t', 'contacts': 'c1'}).text

model = get(f'http://localhost:8080/resume/{pk}').text
print(model)
put('http://localhost:8080/resume', json={
    "contacts": "c2",
    "name": "n1",
    "pk": pk,
    "title": "1t"})
model = get(f'http://localhost:8080/resume/{pk}').text
print(model)
