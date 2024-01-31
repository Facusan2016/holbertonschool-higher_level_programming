const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr'

window.addEventListener('DOMContentLoaded',() => {
  fetch(URL)
  .then((data) => data.json())
  .then((data) => {
    document.querySelector('#hello').textContent = data.hello
  })
})