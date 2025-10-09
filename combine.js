document.addEventListener('DOMContentLoaded', () => {
    const element1Select = document.getElementById('element1');
    const element2Select = document.getElementById('element2');
    const resultDiv = document.getElementById('result');
    const compoundName = document.getElementById('compound-name');
    const element1Info = document.getElementById('element1-info');
    const element2Info = document.getElementById('element2-info');
    const errorMessage = document.getElementById('error-message');

    // Load elements and populate dropdowns
    fetch('/api/elements')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Failed to fetch elements. Status: ${response.status}`);
            }
            return response.json();
        })
        .then(elements => {
            elements.forEach(element => {
                const option1 = document.createElement('option');
                option1.value = element.symbol;
                option1.text = `${element.name} (${element.symbol})`;
                element1Select.add(option1);

                const option2 = document.createElement('option');
                option2.value = element.symbol;
                option2.text = `${element.name} (${element.symbol})`;
                element2Select.add(option2);
            });
        })
        .catch(error => {
            showError(`Error loading elements: ${error.message}`);
        });

    window.combineElements = function() {
        clearError();
        resultDiv.style.display = 'none';

        const symbol1 = element1Select.value;
        const symbol2 = element2Select.value;

        if (!symbol1 || !symbol2) {
            showError("Please select both elements.");
            return;
        }

        if (symbol1 === symbol2) {
            showError("Please select two different elements.");
            return;
        }

        fetch('/api/elements')
            .then(response => response.json())
            .then(elements => {
                const element1 = elements.find(e => e.symbol === symbol1);
                const element2 = elements.find(e => e.symbol === symbol2);

                if (!element1 || !element2) {
                    throw new Error("Element data not found.");
                }

                // Display the compound name
                compoundName.innerText = `${element1.symbol}-${element2.symbol} Compound`;

                // Display detailed info for both elements
                element1Info.innerHTML = generateElementInfo(element1);
                element2Info.innerHTML = generateElementInfo(element2);

                resultDiv.style.display = 'block';
            })
            .catch(error => {
                showError(`Error combining elements: ${error.message}`);
            });
    };

    function generateElementInfo(element) {
        return `
            <h5>${element.name} (${element.symbol})</h5>
            <p><strong>Atomic Number:</strong> ${element.number}</p>
            <p><strong>Atomic Mass:</strong> ${element.mass}</p>
            <p><strong>Group:</strong> ${element.group || 'N/A'}</p>
            <p><strong>Period:</strong> ${element.period}</p>
            <p><strong>Category:</strong> ${element.category}</p>
            <p><strong>Electronegativity:</strong> ${element.en || 'Unknown'}</p>
            <p><strong>Density:</strong> ${element.density || 'Unknown'}</p>
            <p><strong>Melting Point:</strong> ${element.mp || 'Unknown'} °C</p>
            <p><strong>Boiling Point:</strong> ${element.bp || 'Unknown'} °C</p>
        `;
    }

    function showError(message) {
        errorMessage.innerText = message;
        errorMessage.classList.remove('d-none');
    }

    function clearError() {
        errorMessage.innerText = '';
        errorMessage.classList.add('d-none');
    }
});
