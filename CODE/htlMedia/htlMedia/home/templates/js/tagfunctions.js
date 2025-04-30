const tagflexid = "#htagimgwrapper";
let tagflexiconid = "#htagpermaid";
var tag = document.querySelector(tagflexid);



function toggleTagDisplay(){
    if(tag.classList.contains("htagflexhide")){
        tag.classList.remove("htagflexhide");
        document.querySelector(tagflexiconid).classList.remove("fa-chevron-right");
        document.querySelector(tagflexiconid).classList.add("fa-chevron-down");
    }
    else{
        tag.classList.add("htagflexhide");
        document.querySelector(tagflexiconid).classList.remove("fa-chevron-down");
        document.querySelector(tagflexiconid).classList.add("fa-chevron-right");
    }
}