let display = document.querySelector('.todisplay');

function writeToInput(event) {
    let btnval = event.target.value;
    if (btnval === 'C') {
        display.value = '';
        return;
    }
    if (btnval === "=") {
        try {
            display.value = eval(display.value);
        } catch (e) {
            display.value = 'Error';
        }
        return;
    }
    if(btnval==='-1'){
        display.value=-1*eval(display.value);
        return;
    }
    display.value += btnval;
}

document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', writeToInput);
});
