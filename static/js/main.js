// SocialFeed — main.js

// Highlight active nav link on page load
document.addEventListener("DOMContentLoaded", () => {
  // Animate cards with stagger (CSS handles it via animation-delay)
  const cards = document.querySelectorAll(".post-card, .user-card");
  cards.forEach((card, i) => {
    card.style.animationDelay = `${i * 0.05}s`;
  });
});