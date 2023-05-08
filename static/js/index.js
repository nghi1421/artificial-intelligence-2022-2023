let carParkingEnable = false;
let repeatedGuest = false;
const modal = document.getElementById('modal')

function showModal(state) {
    console.log("Nguyen Thanh Nghi");
    console.log(state)
    if (state) {
        modal.classList.remove('hidden')
    }
    else{
        modal.classList.add('hidden')
    }
}

function testing() {
    alert('Canh Bao')
}


function toggleButtonParking () {
const btnToggle = document.getElementById('btnToggleParking');
const circleToggle = document.getElementById('circleToggle');
const cbCarParking = document.getElementById('cbCarParking');
if (!carParkingEnable) {
    btnToggle.classList.add('bg-indigo-600');
    btnToggle.classList.remove('bg-gray-200');
    circleToggle.classList.add('translate-x-5');
    circleToggle.classList.remove('translate-x-0');
    cbCarParking.checked = true;
}
else {
    btnToggle.classList.remove('bg-indigo-600');
    btnToggle.classList.add('bg-gray-200');
    circleToggle.classList.remove('translate-x-5');
    circleToggle.classList.add('translate-x-0');
    cbCarParking.checked = false;
}
carParkingEnable = !carParkingEnable;
}

function toggleButtonRepeat() {
const btnToggleRepeat = document.getElementById('btnToggleRepeat');
const circleToggleRepeat = document.getElementById('circleToggleRepeat');
const cbCarParking = document.getElementById('cbRepeatedGuest');
    if (!repeatedGuest) {
        btnToggleRepeat.classList.add('bg-indigo-600');
        btnToggleRepeat.classList.remove('bg-gray-200');
        circleToggleRepeat.classList.add('translate-x-5');
        circleToggleRepeat.classList.remove('translate-x-0');
        cbCarParking.checked = true;
    }
    else {
        btnToggleRepeat.classList.remove('bg-indigo-600');
        btnToggleRepeat.classList.add('bg-gray-200');
        circleToggleRepeat.classList.remove('translate-x-5');
        circleToggleRepeat.classList.add('translate-x-0');
        cbCarParking.checked = false;
    }
    repeatedGuest = !repeatedGuest;
}