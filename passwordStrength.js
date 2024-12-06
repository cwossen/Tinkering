function checkPasswordStrength(password) {
    let score = 0;
    const length = password.length;

    // 1. Check length
    if (length >= 8 && length <= 12) score += 2;
    else if (length > 12 && length <= 16) score += 3;
    else if (length > 16) score += 5;

    // 2. Check character variety
    if (/[A-Z]/.test(password)) score += 1; // Uppercase letter
    if (/[a-z]/.test(password)) score += 1; // Lowercase letter
    if (/\d/.test(password)) score += 1; // Digit
    if (/[@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]/.test(password)) score += 1; // Special char

    // 3. Penalize common patterns
    const commonPatterns = ["123456", "qwerty", "password", "111111"];
    for (let pattern of commonPatterns) {
        if (password.includes(pattern)) {
            score -= 2;
            break;
        }
    }

    // 4. Penalize repeated characters or substrings
    const repeatPattern = /(.)\1{2,}/; // Detects 3 or more repeated characters
    if (repeatPattern.test(password)) score -= 1;

    // Determine strength based on final score
    if (score <= 2) return { strength: "Weak", color: "red", recommendations: "Try adding a mix of characters and numbers." };
    if (score > 2 && score <= 5) return { strength: "Medium", color: "yellow", recommendations: "Add more special characters and increase length." };
    if (score > 5) return { strength: "Strong", color: "green", recommendations: "Great job! Your password is strong." };
}

// Real-time feedback and UI integration
document.getElementById("password").addEventListener("input", function () {
    const password = this.value;
    const result = checkPasswordStrength(password);

    // Update UI
    document.getElementById("strength").textContent = result.strength;
    document.getElementById("strength-bar").style.backgroundColor = result.color;
    document.getElementById("strength-bar").style.width = result.strength === "Weak" ? "33%" : result.strength === "Medium" ? "66%" : "100%";
    document.getElementById("recommendations").textContent = result.recommendations;
});

// Clear the input and reset UI
document.getElementById("clear-btn").addEventListener("click", function () {
    document.getElementById("password").value = "";
    document.getElementById("strength").textContent = "";
    document.getElementById("strength-bar").style.width = "0%";
    document.getElementById("recommendations").textContent = "";
});

// Example usage in console
const password = "b00b!!**$";
const result = checkPasswordStrength(password);
console.log(`Password: "${password}", Strength: ${result.strength}`);
