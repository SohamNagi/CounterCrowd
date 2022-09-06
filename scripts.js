const btn = document.querySelector('.btn'),
  input = document.querySelector('.input');

btn.addEventListener('click', () => {
  btn.classList.toggle('close');
  input.classList.toggle('inclicked');
});

function changeFormAction() {
    var item = document.getElementById("item").value;
    var form = this;
    form.action = window.location.href + "\multi\" + item;
    form.submit();
  }