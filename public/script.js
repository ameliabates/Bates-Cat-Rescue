// script.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('catForm');

    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(form);
            const catInfo = {};
            formData.forEach((value, key) => {
                catInfo[key] = value;
            });

            saveCatToStorage(catInfo);
            form.reset();
            
        });
    } else {
        console.error("Form with ID 'catForm' not found");
    }

    function saveCatToStorage(cat) {
        let cats = JSON.parse(localStorage.getItem('cats')) || [];
        cats.push(cat);
        localStorage.setItem('cats', JSON.stringify(cats));
    }
});

