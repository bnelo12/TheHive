var editor = ace.edit("editor");
editor.setTheme("ace/theme/twilight");
editor.session.setMode("ace/mode/python");

document.getElementById('sendCodeButton').addEventListener('click', handleSendCode);

var socket = io();

function handleSendCode() {
    const code = editor.getValue();
    socket.emit('webapp_code_send', code);
    document.getElementById('editor').remove();
    document.getElementById('sendCodeButton').remove();
    const cardBody = document.getElementsByClassName('card-body')[0];
    cardBody.innerHTML += '<br /><br /><div class="loader"></div><h5>Running...</h5><br /><br />';
    socket.on('finished', (result) => {
        cardBody.getElementsByTagName('h5')[1].textContent = `Result: ${result}`;
        document.getElementsByClassName('loader')[0].remove();
    });
}
