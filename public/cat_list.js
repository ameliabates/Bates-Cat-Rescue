document.addEventListener('DOMContentLoaded', function() {
    const catList = document.getElementById('catList');
    if (!catList) {
        console.error("Element with ID 'catList' not found");
        return;
    }

    const cats = JSON.parse(localStorage.getItem('cats')) || [];
    cats.forEach(cat => {
        const catDiv = document.createElement('div');
        catDiv.classList.add('cat');
        catDiv.innerHTML = `
            <h2>${cat.name}</h2>
            <p>Age: ${cat.age}</p>
            <p>Breed: ${cat.breed}</p>
            <p>Gender: ${cat.gender}</p>
            <p>Color: ${cat.color}</p>
            <p>Description: ${cat.description}</p>
        `;
        catList.appendChild(catDiv);
    });
});
