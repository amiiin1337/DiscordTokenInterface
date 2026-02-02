document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('login-btn');
    const tokenInput = document.getElementById('token-input');
    const loginBlock = document.querySelector('.login-block');

    loginBtn.addEventListener('click', () => {
        const token = tokenInput.value.trim();

        if (token) {
            console.log('Token entered:', token);
            loginBtn.innerHTML = '<div>Launching...</div>';
            loginBtn.style.backgroundColor = '#43b581';

            // Send to Backend
            fetch('http://localhost:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ token: token })
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                    //  new Chrome window
                })
                .catch((error) => {
                    console.error('Error:', error);
                    alert('Error connecting to backend. Is server.py running?');
                })
                .finally(() => {
                    setTimeout(() => {
                        loginBtn.innerHTML = '<div>Log In</div>';
                        loginBtn.style.backgroundColor = '';
                    }, 3000);
                });

        } else {
            loginBlock.animate([
                { transform: 'translateX(0)' },
                { transform: 'translateX(-10px)' },
                { transform: 'translateX(10px)' },
                { transform: 'translateX(-10px)' },
                { transform: 'translateX(10px)' },
                { transform: 'translateX(0)' }
            ], {
                duration: 300
            });
            tokenInput.focus();
            tokenInput.style.borderColor = '#fa777c';
            setTimeout(() => {
                tokenInput.style.borderColor = '';
            }, 2000);
        }
    });

    tokenInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            loginBtn.click();
        }
    });
});
