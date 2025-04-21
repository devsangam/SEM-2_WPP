    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    const closeBtn = document.getElementById('close-btn');
    
    hamburger.addEventListener('click', () => {
      navMenu.classList.add('active');
      hamburger.style.display = 'none';
    });
    
    closeBtn.addEventListener('click', () => {
      navMenu.classList.remove('active');
      hamburger.style.display = 'flex';
    });
