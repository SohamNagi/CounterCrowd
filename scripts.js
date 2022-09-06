const btn = document.querySelector('.btn'),
  input = document.querySelector('.input');

btn.addEventListener('click', () => {
  btn.classList.toggle('close');
  input.classList.toggle('inclicked');
});