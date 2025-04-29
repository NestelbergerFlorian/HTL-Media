const tagflexid = "#tagimgwrapper";
let tagflexiconid = "#tagpermaid";
var tag = document.querySelector(tagflexid);

function toggleTagDisplay(){
    if(tag.classList.contains("tagflexhide")){
        tag.classList.remove("tagflexhide");
        document.querySelector(tagflexiconid).classList.remove("fa-chevron-right");
        document.querySelector(tagflexiconid).classList.add("fa-chevron-down");
    }
    else{
        tag.classList.add("tagflexhide");
        document.querySelector(tagflexiconid).classList.remove("fa-chevron-down");
        document.querySelector(tagflexiconid).classList.add("fa-chevron-right");
    }
}