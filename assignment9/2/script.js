function Nav() {
    var x = document.getElementById("NavList");
    if (x.className === "nav_list") {
      x.className += " clicked";
    } else {
      x.className = "nav_list";
    }
  }

function deptNav() {
    var x = document.getElementById("Department");
    if (x.className === "department") {
      x.className += " clicked";
    } else {
      x.className = "department";
    }
}

var img=1
function left(){
  var current = document.getElementById(String(img));
  current.className="hidden";
  if(img<=1){
    img=4;
  } else {
    img=(img-1);
  }
  var next=document.getElementById(String(img));
  next.className="display";
}

function right(){  
  var current = document.getElementById(String(img));
  current.className="hidden";
  if(img>=4){
    img=1;
  } else {
    img=img+1;
  }
  var next=document.getElementById(String(img));
  next.className="display";
}