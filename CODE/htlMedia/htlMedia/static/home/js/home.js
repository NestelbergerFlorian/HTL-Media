const sessionUser = document.getElementById("user").getAttribute("user");
console.log(sessionUser);

<<<<<<< HEAD
=======
function backButtonClick() {
    displaySideBar(false);
}

function toggleLikeFilled(){
    document.querySelector('#likebtn').classList.toggle('fa-heart');
    document.querySelector('#likebtn').classList.toggle('fa-heart-circle-check');
}

function displaySideBar(display){
    if(display){
        document.getElementById("sidebar").style.display = "flex"
    }else{
        document.getElementById("sidebar").style.display = "none"
    }
}

function activateUploadform() {
    document.getElementById("form-container").style.display = "flex";
}

const hamburgerbutton = document.getElementById("hhamburger").addEventListener("click",(event) => {hamburgerClick()});
const backButton =      document.getElementById("backButton").addEventListener("click",(event) => {backButtonClick()});
const upload =          document.getElementById("uploadButton").addEventListener("click",(event) => {activateUploadform()});

const DarkLightModeToggle = document.getElementById("DarkLightModeToggle");
if (DarkLightModeToggle.checked) {
    const Html = document.getElementById("html"); 
Html.setAttribute("data-theme", "light");
}
>>>>>>> 96ec5e208d7dbe00dd437401a24af052edf33bb0
