let tagflexiconid = "#tagpermaid";
var tag = document.querySelector(tagflexiconid);



/*function toggleTagDisplay(){
    console.log("start");
    if(tag.classList.contains("showing")){
        console.log("entered1");
        tag.classList.remove("showing");
        tag.classList.add("hiding");
        tag.classList.remove("rotate-90");
    }
    else if(tag.classList.contains("hiding")){
        console.log("entered1");
        tag.classList.remove("hiding");
        tag.classList.add("showing");
        tag.classList.add("rotate-90");
    }
}*/

let menus = document.querySelectorAll('.well');
for (const menu of menus) {
    menu.addEventListener('click', function(event) {
    this.classList.toggle('collapsed');
    let titleDiv = this.querySelector('.collapse-title');
    if (titleDiv) {
        const icon = titleDiv.querySelector('svg');
        if (icon) {
            icon.classList.toggle('rotate-90');
        }
    }
    })
}