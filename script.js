document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('login-btn');
    const tokenInput = document.getElementById('token-input');
    const loginBlock = document.querySelector('.login-block');

    loginBtn.addEventListener('click', () => {
        const token = tokenInput.value.trim();

        if (token) {
            console.log('Token entered:', token);
            loginBtn.innerHTML = '<div>Verifying...</div>';
            loginBtn.style.backgroundColor = '#43b581';

            setTimeout(() => {
                alert(`Logged in with token: ${token}`);
                loginBtn.innerHTML = '<div>Log In</div>';
                loginBtn.style.backgroundColor = '';
            }, 1000);
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
