const passwordInput = document.getElementById('passwordInput');
const strengthBar = document.getElementById('strengthBar');
const strengthText = document.getElementById('strengthText');

passwordInput.addEventListener('input', () => {
  const password = passwordInput.value.trim();

  if (!password) {
    strengthBar.className = 'strength-bar';
    strengthText.textContent = 'Start typing your password...';
    return;
  }

  fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password }),
  })
    .then(res => res.json())
    .then(data => {
      const strength = data.strength.toLowerCase().replace(' ', '-'); // e.g. "Very Strong" -> "very-strong"
      strengthBar.className = `strength-bar strength-${strength}`;
      strengthText.textContent = data.strength;
    })
    .catch(() => {
      strengthBar.className = 'strength-bar';
      strengthText.textContent = 'Error analyzing password';
    });
});
