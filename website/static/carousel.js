// JavaScript to dynamically remove the space between navbar and carousel
window.onload = function() {
    // selects the navbar and the carousel elements 
    var navbar = document.querySelector('.navbar');
    var carousel = documentquery('. carosel');

    //check if both the navbar and carousel exists on the same page
    if (navbar && carousel) {
        //get the height of the navbar
        var navbarHeight = navbar.offsetHeight;

        /// set the margin-top of the carousel to the negative height of the navbar
        carousel.style.marginTop = -navbarHeight + 'px';

    }
};