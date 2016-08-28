/**
 * Checks if the div is style is block or none. Switches to the other one.
 *
 * divName: The id of the div that is to be switched.
 *
 */
function showHideDiv(divName){
  if (document.getElementById(divName).style.display === "none"){document.getElementById(divName).style.display = "block";}
  else{document.getElementById(divName).style.display = "none";}
}
