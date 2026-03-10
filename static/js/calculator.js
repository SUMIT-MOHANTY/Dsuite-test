document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculator-form');
    const num1Input = document.getElementById('num1-input');
    const operationSelect = document.getElementById('operation-select');
    const num2Input = document.getElementById('num2-input');
    const submitButton = form.querySelector('[type="submit"]');
    const result = document.getElementById('result');
    
    // Handle form submission via AJAX
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const data = {
            num1: parseFloat(formData.get('num1')),
            num2: parseFloat(formData.get('num2')),
            operation: formData.get('operation')
        };
        
        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            const resultData = await response.json();
            
            if (resultData.success) {
                result.textContent = `Result: ${resultData.result}`;
            } else {
                result.textContent = `Error: ${resultData.error}`;
            }
            
            // Return focus to result for screen reader announcement
            result.focus();
            
        } catch (error) {
            result.textContent = 'Error: Connection failed';
            result.focus();
        }
    });
    
    // Trap Tab navigation within form
    form.addEventListener('keydown', function(e) {
        const elements = [num1Input, operationSelect, num2Input, submitButton];
        const currentIndex = elements.indexOf(document.activeElement);
        
        if (e.key === 'Tab' && !e.shiftKey && currentIndex === elements.length - 1) {
            e.preventDefault();
            num1Input.focus();
        } else if (e.key === 'Tab' && e.shiftKey && currentIndex === 0) {
            e.preventDefault();
            submitButton.focus();
        }
    });
    
    // Enter and Space keys on submit button
    submitButton.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            form.dispatchEvent(new Event('submit'));
        }
    });
});
