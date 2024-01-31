document.querySelector('#toggle_header').addEventListener('click',() => {
  const header = document.querySelector('header')
  header.classList.contains('green')
  ?
  (
    header.classList.remove('green'),
    header.classList.add('red')
  )
  :
  (
    header.classList.add('green'),
    header.classList.remove('red')
  )
})