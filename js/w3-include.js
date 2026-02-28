function includeHTML() {
  var z, i, elmnt, file, xhttp;
  /* Loop through all HTML elements */
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /* Search for elements with a w3-include-html attribute */
    file = elmnt.getAttribute("w3-include-html");
    if (file) {
      /* Make an HTTP request with the attribute value as the file name */
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {
            var content = this.responseText;
            /* Adjust paths if we're in a subdirectory */
            if (window.location.pathname.includes('/user-guide/')) {
              /* We're in user-guide directory, adjust navbar paths to go up one level */
              content = content.replace(/href="index\.html"/g, 'href="../index.html"');
              content = content.replace(/href="freebirdapplication\.html"/g, 'href="../freebirdapplication.html"');
              content = content.replace(/href="nextgen\.html"/g, 'href="../nextgen.html"');
              content = content.replace(/href="documentation\.html"/g, 'href="../documentation.html"');
            }
            elmnt.innerHTML = content;
          }
          if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
          /* Remove the attribute, and call this function once more */
          elmnt.removeAttribute("w3-include-html");
          includeHTML();
        }
      }
      xhttp.open("GET", file, true);
      xhttp.send();
      /* Exit the function */
      return;
    }
  }
  /* After all includes are loaded, update active menu item */
  updateActiveMenuItem();
}

function updateActiveMenuItem() {
  /* Get current page filename */
  var currentPage = window.location.pathname.split("/").pop();
  if (currentPage === "") currentPage = "index.html";
  
  /* Remove active class from all menu items */
  var menuItems = document.querySelectorAll('.menu-1 li');
  menuItems.forEach(function(item) {
    item.classList.remove('active');
  });
  
  /* Add active class to current page menu item */
  var links = document.querySelectorAll('.menu-1 a');
  links.forEach(function(link) {
    var linkPage = link.getAttribute('href');
    if (linkPage === currentPage) {
      link.parentElement.classList.add('active');
    }
  });
}

/* Call includeHTML when DOM is ready */
document.addEventListener('DOMContentLoaded', function() {
  includeHTML();
});