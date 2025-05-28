function hamburgerClick() {
    displaySideBar(true);
}

function backButtonClick() {
    displaySideBar(false);
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

function postClick(event){
    let view = document.getElementById("view-container");
    view.style.display = "flex";
    view.appendChild(event.target.cloneNode(true));
    
}

function disablePostview(event){
    let view = event.target;
    view.removeChild(view.lastElementChild);
    view.style.display = "none";
}

const hamburgerbutton = document.getElementById("hhamburger").addEventListener("click",(event) => { hamburgerClick()});
const backButton =      document.getElementById("backButton").addEventListener("click",(event) => {backButtonClick()});
const upload =          document.getElementById("uploadButton").addEventListener("click",(event) => {activateUploadform()});
const view =            document.getElementById("view-container").addEventListener("click",(event) => { disablePostview(event)})
const posts =           document.getElementsByClassName("postPic");

for (var i = 0; i < posts.length; i++) {
    posts[i].addEventListener("click",(event) => {postClick(event)})
}



const DarkLightModeToggle = document.getElementById("DarkLightModeToggle");
if (DarkLightModeToggle.checked) {
    const Html = document.getElementById("html"); 
    Html.setAttribute("data-theme", "light");
}