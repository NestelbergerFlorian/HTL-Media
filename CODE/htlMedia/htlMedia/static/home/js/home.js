function hamburgerClick() {
    displaySideBar(true);
}

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