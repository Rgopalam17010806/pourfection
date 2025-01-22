// JavaScript to handle modal interactions
// Add event listeners to each 'Select' button
document.querySelectorAll('.select-recipe').forEach(button => {
    button.addEventListener('click', function () {
        const recipeId = this.getAttribute('data-recipe-id');
        // Store the recipe ID in sessionStorage for use later
        sessionStorage.setItem('selectedRecipeId', recipeId);
    });
});

// Add event listener to the 'Confirm' button in the modal
document.getElementById('confirmSize').addEventListener('click', function () {
    const selectedSize = document.querySelector('input[name="size"]:checked')?.value;
    const recipeId = sessionStorage.getItem('selectedRecipeId'); // This retrieves the stored recipe ID

    if (selectedSize && recipeId) {
        // Create a form to submit the order
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = '/submit_order';

        // Create hidden input fields for recipeID and size
        const recipeInput = document.createElement('input');
        recipeInput.type = 'hidden';
        recipeInput.name = 'recipe_id';
        recipeInput.value = recipeId; // Correct variable name here
        form.appendChild(recipeInput);

        const sizeInput = document.createElement('input');
        sizeInput.type = 'hidden';
        sizeInput.name = 'size';
        sizeInput.value = selectedSize;
        form.appendChild(sizeInput);

        document.body.appendChild(form);
        form.submit();
    } else {
        alert("Please select a size.");
    }
});

