const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

fetch(URL)
.then((data) => {
  return data.json()
})
.then((data) => {
  document.querySelector('#character').textContent = data.name
})