document.addEventListener('DOMContentLoaded', () => {
  // 1. Set current year in footer
  const yearSpan = document.getElementById('year');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }

  // 2. Sticky Header
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // 3. Mobile Hamburger Menu Toggle
  const openBtn = document.querySelector('.nav-open-btn');
  const closeBtn = document.querySelector('.nav-close-btn');
  const nav = document.querySelector('.navbar');
  const overlay = document.querySelector('.overlay');

  const toggleNav = () => {
    nav.classList.toggle('active');
    overlay.classList.toggle('active');
  };

  if (openBtn && closeBtn && nav && overlay) {
    openBtn.addEventListener('click', toggleNav);
    closeBtn.addEventListener('click', toggleNav);
    overlay.addEventListener('click', toggleNav);
  }

  // 4. Initialize AOS Animation Library
  if (typeof AOS !== 'undefined') {
    AOS.init({
      once: true,
      offset: 50,
    });
  }

  // 5. Stats Counter Animation
  const counters = document.querySelectorAll('.stat-number');
  
  if (counters.length > 0) {
    const counterObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const targetStr = entry.target.getAttribute('data-count');
          if (!targetStr) return;
          const target = parseInt(targetStr, 10);
          const duration = 2000;
          const stepTime = Math.abs(Math.floor(duration / target));
          let current = 0;
          
          const timer = setInterval(() => {
            current += Math.ceil(target / 100) || 1;
            if (current >= target) {
              current = target;
              clearInterval(timer);
            }
            entry.target.textContent = current + (entry.target.getAttribute('data-suffix') || '');
          }, stepTime);
          
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
      counterObserver.observe(counter);
    });
  }

  // 6. FAQ Accordion
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
      const isActive = question.classList.contains('active');
      
      // Close all other questions (optional, creates accordion effect)
      faqQuestions.forEach(q => q.classList.remove('active'));
      
      // Toggle current
      if (!isActive) {
        question.classList.add('active');
      }
    });
  });
});

// 7. Contact Form Handler (Mock)
function handleContactSubmit(event) {
    event.preventDefault();
    const successMsg = document.getElementById('form-success');
    if (successMsg) {
        successMsg.style.display = 'block';
        event.target.reset();
        
        setTimeout(() => {
            successMsg.style.display = 'none';
        }, 5000);
    }
}

// 8. Tracking Form Handler (Mock)
function handleTrackingSubmit(event) {
    event.preventDefault();
    const lrNumber = document.getElementById('lr-number').value;
    const results = document.getElementById('tracking-results');
    const displayLr = document.getElementById('display-lr');
    
    if (results && displayLr) {
        displayLr.textContent = lrNumber;
        results.classList.add('active');
    }
}

// 9. Gallery Lightbox
function openLightbox(imageSrc) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    
    if (lightbox && lightboxImg) {
        lightboxImg.innerHTML = `<img src="${imageSrc}" alt="Gallery View" style="max-width:100%; max-height:80vh; border-radius:4px; object-fit:contain;">`;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeLightbox(event) {
    if (event.target.classList.contains('lightbox') || event.target.classList.contains('lightbox-close')) {
        const lightbox = document.getElementById('lightbox');
        if (lightbox) {
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
        }
    }
}
