var x = document.getElementById("audio"); 

function pauseAudio() { 
    x.pause(); 
} 

function playAudio() {
    x.play();
}


// PopUp : About.

var aboutModal = document.getElementById("about");
var btnAbout = document.getElementById("btnAbout");
var span = document.getElementsByClassName("close")[0];


btnAbout.onclick = function() {
    aboutModal.style.display = "block";
}

span.onclick = function() {
    aboutModal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == aboutModal) {
    aboutModal.style.display = "none";
  }



}

		// PopUp: Instructions.

    var instructionsModal = document.getElementById("myInstructionsModal");
    var btnInstructions = document.getElementById("myBtnInstructions");
    var span2 = document.getElementsByClassName("close")[1];
    
    btnInstructions.onclick = function() {
      instructionsModal.style.display = "block";
    }
    
    span2.onclick = function() {
      instructionsModal.style.display = "none";
    }
    
    window.onclick = function(event) { 
      if (event.target == instructionsModal) {
        instructionsModal.style.display = "none";
      }
    }