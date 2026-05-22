console.log("JS Connected");
// RESPONSIVE NAVBAR ICON
const menuIcon = document.getElementById("menu-icon");
const mobileMenu = document.getElementById("mobile-menu");

menuIcon.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden");
});


// TEXTS TO TYPE
const texts = [
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "UI/UX Designer"
];

let count = 0;
let index = 0;
let currentText = "";
let letter = "";


// BOTH ELEMENTS
const typingDesktop = document.getElementById("typing");
const typingMobile = document.getElementById("typing-mobile");


// TYPE FUNCTION
function type() {

    if (count === texts.length) {
        count = 0;
    }

    currentText = texts[count];

    letter = currentText.slice(0, ++index);

    // DESKTOP
    if (typingDesktop) {
        typingDesktop.textContent = letter;
    }

    // MOBILE
    if (typingMobile) {
        typingMobile.textContent = letter;
    }

    // WHEN WORD COMPLETES
    if (letter.length === currentText.length) {

        setTimeout(() => {
            erase();
        }, 1500);

    } else {

        setTimeout(type, 100);

    }
}


// ERASE FUNCTION
function erase() {

    letter = currentText.slice(0, --index);

    // DESKTOP
    if (typingDesktop) {
        typingDesktop.textContent = letter;
    }

    // MOBILE
    if (typingMobile) {
        typingMobile.textContent = letter;
    }

    // MOVE TO NEXT WORD
    if (letter.length === 0) {

        count++;

        setTimeout(type, 300);

    } else {

        setTimeout(erase, 50);

    }
}


// START TYPING
type();


// RESUME DOWNLOAD
function downloadCV() {

    const link = document.createElement("a");

    // resumeURL comes from HTML
    link.href = resumeURL;

    link.download = "My_Resume.pdf";

    link.click();
}