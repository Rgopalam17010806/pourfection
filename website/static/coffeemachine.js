// JavaScript to handle modal interactions
document.querySelectorAll('.select-recipe').forEach(button => {
    button.addEventListener('click', function () {
        const recipeId = this.getAttribute('data-recipe-id');
        //store the recipe ID in sessionStorage for use later
        sessionStorage.setItem('selectedRecipeId', recipeId);
    });
});

document.getElementById('confirmSize').addEventListener('click', function () {
    const selectedSize = document.querySelector('input[name="size"]:checked')?.value;
    const recipeId = sessionStorage.getItem('selectedRecipeId'); //this retrives the stored recipe ID

    if (selectedSize && recipeId) {
        // Redirect the user to the prepare page with the recipeID and the size. 
        window.location.href =  `/prepare/${recipeId}?size=${selectedSize}`;
    } else {
        alert("Please select a size. ");
    }
});
