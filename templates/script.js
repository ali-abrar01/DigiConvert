document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const convertBtn = document.getElementById('convert-btn');
    const inputField = document.getElementById('input-value');
    const typeSelect = document.getElementById('conversion-type');
    const resultCard = document.getElementById('result-card');
    const outputValue = document.getElementById('output-value');
    const stepsContent = document.getElementById('steps-content');
    const toggleStepsBtn = document.getElementById('toggle-steps');
    const errSpan = document.getElementById('input-error');
    const copyBtn = document.getElementById('copy-btn');

    // Set initial icon based on body class
    if (body.classList.contains('dark-mode')) {
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }

    // Theme Toggle
    themeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        const isDark = body.classList.contains('dark-mode');
        themeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    });

    // Validation patterns
    const patterns = {
        'bin2dec': { regex: /^[01]+$/, msg: 'Only 0 and 1 allowed' },
        'dec2bin': { regex: /^\d+$/, msg: 'Only decimal digits allowed' },
        'bin2gray': { regex: /^[01]+$/, msg: 'Only 0 and 1 allowed' },
        'gray2bin': { regex: /^[01]+$/, msg: 'Only 0 and 1 allowed' }
    };

    const placeholders = {
        'bin2dec': 'e.g., 1010',
        'dec2bin': 'e.g., 38',
        'bin2gray': 'e.g., 1010',
        'gray2bin': 'e.g., 1011'
    };

    function validateInput() {
        const type = typeSelect.value;
        const val = inputField.value.trim();
        
        if (!val) {
            showError('');
            return false;
        }

        const rule = patterns[type];
        if (!rule.regex.test(val)) {
            showError(rule.msg);
            return false;
        }

        showError(''); // Clear error
        return true;
    }

    function showError(msg) {
        errSpan.textContent = msg;
        if (msg) errSpan.classList.add('visible');
        else errSpan.classList.remove('visible');
    }

    inputField.addEventListener('input', validateInput);
    typeSelect.addEventListener('change', () => {
        inputField.placeholder = placeholders[typeSelect.value];
        inputField.value = '';
        showError('');
        resultCard.classList.remove('visible');
    });

    // Convert Action
    convertBtn.addEventListener('click', async () => {
        if (!validateInput()) return;
        
        const type = typeSelect.value;
        const value = inputField.value.trim();
        if (!value) return;

        // Button Loading State
        const originalBtnText = convertBtn.innerHTML;
        convertBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Converting...';
        convertBtn.disabled = true;

        try {
            const response = await fetch('/convert', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ type, value })
            });

            const data = await response.json();

            if (response.ok) {
                // Show Result
                resultCard.classList.remove('visible'); // Reset animation
                setTimeout(() => resultCard.classList.add('visible'), 10);
                
                outputValue.textContent = data.result;
                
                // Render Steps
                stepsContent.innerHTML = '';
                data.steps.forEach(step => {
                    const div = document.createElement('div');
                    div.className = 'step-item';
                    div.textContent = step;
                    stepsContent.appendChild(div);
                });
            } else {
                showError(data.error || 'Conversion failed');
            }

        } catch (error) {
            console.error('Error:', error);
            showError('Network error. Check connection.');
        } finally {
            convertBtn.innerHTML = originalBtnText;
            convertBtn.disabled = false;
        }
    });

    // Copy to Clipboard
    copyBtn.addEventListener('click', () => {
        const text = outputValue.textContent;
        navigator.clipboard.writeText(text).then(() => {
            const originalIcon = copyBtn.innerHTML;
            copyBtn.innerHTML = '<i class="fas fa-check"></i>';
            setTimeout(() => copyBtn.innerHTML = originalIcon, 1500);
        });
    });

    // Toggle Steps
    toggleStepsBtn.addEventListener('click', () => {
        stepsContent.classList.toggle('collapsed');
        const isCollapsed = stepsContent.classList.contains('collapsed');
        toggleStepsBtn.innerHTML = isCollapsed 
            ? 'View Step-by-Step Explanation <i class="fas fa-chevron-down"></i>'
            : 'Hide Steps <i class="fas fa-chevron-up"></i>';
    });
});
