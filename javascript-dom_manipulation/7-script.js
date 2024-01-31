const URL = 'https://swapi-api.hbtn.io/api/films/?format=json'

fetch(URL)
.then((data) => {
  return data.json()
})
.then(({ results }) => {
  const ul = document.querySelector('#list_movies')
  results.forEach((e) => {
    let li = document.createElement('li')
    li.textContent = e.title
    ul.appendChild(li)
  })
})