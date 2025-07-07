// DOM yüklendiğinde çalışacak fonksiyonlar
document.addEventListener('DOMContentLoaded', function() {
    // Mobil menü toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // Smooth scroll için tüm linkleri seç
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 80; // Navbar yüksekliği için offset
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
                
                // Mobil menüyü kapat
                if (navMenu.classList.contains('active')) {
                    hamburger.classList.remove('active');
                    navMenu.classList.remove('active');
                }
            }
        });
    });

    // Navbar scroll efekti
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(10, 10, 10, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(255, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    });

    // Scroll animasyonları
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Animasyon için elementleri seç
    const animateElements = document.querySelectorAll('.team-content, .drivers-grid, .car-showcase, .news-grid, .driver-card, .news-card');
    
    animateElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });

    // İstatistik sayaç animasyonu
    const stats = document.querySelectorAll('.stat-number');
    
    const animateCounter = (element, target) => {
        let current = 0;
        const increment = target / 100;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current);
        }, 20);
    };

    // İstatistikleri gözlemle
    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.textContent);
                animateCounter(entry.target, target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    stats.forEach(stat => {
        statsObserver.observe(stat);
    });

    // CTA button hover efekti
    const ctaButton = document.querySelector('.cta-button');
    
    if (ctaButton) {
        ctaButton.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.05)';
        });
        
        ctaButton.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        ctaButton.addEventListener('click', function() {
            // Smooth scroll to team section
            const teamSection = document.querySelector('#team');
            if (teamSection) {
                teamSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }

    // Parallax efekti için hero section
    const hero = document.querySelector('.hero');
    
    window.addEventListener('scroll', function() {
        if (hero) {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            hero.style.transform = `translateY(${rate}px)`;
        }
    });

    // Driver kartları için hover efektleri
    const driverCards = document.querySelectorAll('.driver-card');
    
    driverCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) scale(1.02)';
            this.style.boxShadow = '0 25px 50px rgba(255, 0, 0, 0.3)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 20px 40px rgba(255, 0, 0, 0.2)';
        });
    });

    // News kartları için hover efektleri
    const newsCards = document.querySelectorAll('.news-card');
    
    newsCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
            this.style.boxShadow = '0 20px 40px rgba(255, 0, 0, 0.3)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 15px 30px rgba(255, 0, 0, 0.2)';
        });
    });

    // Typing efekti için hero title
    const heroTitle = document.querySelector('.hero-title');
    
    if (heroTitle) {
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        
        let i = 0;
        const typeWriter = () => {
            if (i < text.length) {
                heroTitle.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        // Typing efektini başlat
        setTimeout(typeWriter, 1000);
    }

    // Loading animasyonu
    window.addEventListener('load', function() {
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.5s ease';
        
        setTimeout(() => {
            document.body.style.opacity = '1';
        }, 100);
    });

    // Scroll to top button
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.innerHTML = '🏎️';
    scrollToTopBtn.className = 'scroll-to-top';
    scrollToTopBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(45deg, #ff0000, #cc0000);
        color: white;
        border: none;
        cursor: pointer;
        font-size: 1.5rem;
        box-shadow: 0 5px 15px rgba(255, 0, 0, 0.3);
        transition: all 0.3s ease;
        z-index: 1000;
        opacity: 0;
        visibility: hidden;
    `;
    
    document.body.appendChild(scrollToTopBtn);
    
    // Scroll to top button görünürlüğü
    window.addEventListener('scroll', function() {
        if (window.scrollY > 500) {
            scrollToTopBtn.style.opacity = '1';
            scrollToTopBtn.style.visibility = 'visible';
        } else {
            scrollToTopBtn.style.opacity = '0';
            scrollToTopBtn.style.visibility = 'hidden';
        }
    });
    
    // Scroll to top functionality
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Hover efektleri
    scrollToTopBtn.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.1)';
        this.style.boxShadow = '0 8px 25px rgba(255, 0, 0, 0.4)';
    });
    
    scrollToTopBtn.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
        this.style.boxShadow = '0 5px 15px rgba(255, 0, 0, 0.3)';
    });

    // Preloader animasyonu
    const preloader = document.createElement('div');
    preloader.className = 'preloader';
    preloader.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: #0a0a0a;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        transition: opacity 0.5s ease;
    `;
    
    preloader.innerHTML = `
        <div style="text-align: center;">
            <div style="font-size: 3rem; color: #ff0000; margin-bottom: 1rem;">🏎️</div>
            <div style="color: #ff0000; font-family: 'Racing Sans One', cursive; font-size: 1.5rem;">SCUDERIA FERRARI</div>
        </div>
    `;
    
    document.body.appendChild(preloader);
    
    // Preloader'ı kaldır
    setTimeout(() => {
        preloader.style.opacity = '0';
        setTimeout(() => {
            preloader.remove();
        }, 500);
    }, 2000);

    // Konfeti efekti (CTA button'a tıklandığında)
    function createConfetti() {
        const colors = ['#ff0000', '#cc0000', '#ffffff', '#ffcc00'];
        
        for (let i = 0; i < 50; i++) {
            const confetti = document.createElement('div');
            confetti.style.cssText = `
                position: fixed;
                width: 10px;
                height: 10px;
                background: ${colors[Math.floor(Math.random() * colors.length)]};
                top: -10px;
                left: ${Math.random() * window.innerWidth}px;
                animation: confetti-fall 3s linear forwards;
                z-index: 1001;
            `;
            
            document.body.appendChild(confetti);
            
            setTimeout(() => {
                confetti.remove();
            }, 3000);
        }
    }
    
    // Confetti animasyonu için CSS ekle
    const style = document.createElement('style');
    style.textContent = `
        @keyframes confetti-fall {
            to {
                transform: translateY(${window.innerHeight}px) rotate(360deg);
            }
        }
    `;
    document.head.appendChild(style);
    
    // CTA button'a confetti efekti ekle
    if (ctaButton) {
        ctaButton.addEventListener('click', createConfetti);
    }

    // Performans optimizasyonu için throttle fonksiyonu
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        }
    }

    // Scroll event'lerini throttle et
    const throttledScroll = throttle(function() {
        // Scroll event'leri burada
    }, 16); // ~60fps

    window.addEventListener('scroll', throttledScroll);

    // Araba Slideshow
    const carSlides = document.querySelectorAll('.car-slide');
    const indicators = document.querySelectorAll('.indicator');
    let currentSlide = 0;
    let slideInterval;

    function showSlide(index) {
        // Tüm slide'ları gizle
        carSlides.forEach(slide => slide.classList.remove('active'));
        indicators.forEach(indicator => indicator.classList.remove('active'));
        
        // Aktif slide'ı göster
        carSlides[index].classList.add('active');
        indicators[index].classList.add('active');
        
        currentSlide = index;
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % carSlides.length;
        showSlide(currentSlide);
    }

    function startSlideshow() {
        slideInterval = setInterval(nextSlide, 3000); // 3 saniyede bir değiş
    }

    function stopSlideshow() {
        clearInterval(slideInterval);
    }

    // Indicator'lara tıklama olayı
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            showSlide(index);
            stopSlideshow();
            startSlideshow(); // Timer'ı yeniden başlat
        });
    });

    // Slideshow'u başlat
    if (carSlides.length > 0) {
        startSlideshow();
        
        // Mouse hover olduğunda durdur
        const carSlideshow = document.querySelector('.car-slideshow');
        if (carSlideshow) {
            carSlideshow.addEventListener('mouseenter', stopSlideshow);
            carSlideshow.addEventListener('mouseleave', startSlideshow);
        }
    }
});

// Sayfa yüklendiğinde çalışacak ek fonksiyonlar
window.addEventListener('load', function() {
    // Tüm resimlerin yüklendiğinden emin ol
    const images = document.querySelectorAll('img');
    let loadedImages = 0;
    
    images.forEach(img => {
        if (img.complete) {
            loadedImages++;
        } else {
            img.addEventListener('load', () => {
                loadedImages++;
            });
        }
    });
    
    // Sayfa tamamen yüklendiğinde
    if (loadedImages === images.length) {
        document.body.classList.add('loaded');
    }
});

// GENEL PERFORMANS ANALİZİ (Yıllara Göre Galibiyet ve Puan)
Papa.parse('Analyse/ferrari_yillik_ozet.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        const years = data.map(row => row['year']);
        const galibiyet = data.map(row => Number(row['Galibiyet']));
        const puan = data.map(row => Number(row['Puan']));
        const ctx = document.getElementById('ferrariGenelPerformansChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: years,
                datasets: [
                    {
                        label: 'Galibiyet',
                        data: galibiyet,
                        backgroundColor: 'rgba(255,0,0,0.7)'
                    },
                    {
                        label: 'Puan',
                        data: puan,
                        type: 'line',
                        borderColor: 'rgba(200,0,0,1)',
                        backgroundColor: 'rgba(200,0,0,0.1)',
                        yAxisID: 'y1',
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                interaction: { mode: 'index', intersect: false },
                stacked: false,
                plugins: {
                    legend: { display: true },
                    title: { display: true, text: 'Yıllara Göre Galibiyet ve Puan' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Galibiyet' } },
                    y1: {
                        beginAtZero: true,
                        position: 'right',
                        grid: { drawOnChartArea: false },
                        title: { display: true, text: 'Puan' }
                    }
                }
            }
        });
    }
});

// PİLOT PERFORMANS ANALİZİ (En Çok Puan Alan 10 Pilot)
Papa.parse('Analyse/ferrari_en_cok_puan_pilotlar.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        const pilots = data.map(row => row['driver_name']);
        const puan = data.map(row => Number(row['Puan']));
        const ctx = document.getElementById('ferrariPilotPerformansChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: pilots,
                datasets: [
                    {
                        label: 'Puan',
                        data: puan,
                        backgroundColor: 'rgba(255,0,0,0.7)'
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: { display: true, text: 'En Çok Puan Alan 10 Ferrari Pilotu' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Puan' } }
                }
            }
        });
    }
});

// PİST PERFORMANS ANALİZİ (En Çok Kazanılan 10 Pist)
Papa.parse('Analyse/ferrari_en_cok_kazanilan_pistler.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        const pistler = data.map(row => row['name_circuit']);
        const galibiyet = data.map(row => Number(row['Galibiyet']));
        const ctx = document.getElementById('ferrariPistPerformansChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: pistler,
                datasets: [
                    {
                        label: 'Galibiyet',
                        data: galibiyet,
                        backgroundColor: 'rgba(255,0,0,0.7)'
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: { display: true, text: 'En Çok Kazanılan 10 Pist' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Galibiyet' } }
                }
            }
        });
    }
});

// YILLIK PERFORMANS ANALİZİ (Yıllara Göre Podyum)
Papa.parse('Analyse/ferrari_yillik_ozet.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        const years = data.map(row => row['year']);
        const podyum = data.map(row => Number(row['Podyum']));
        const ctx = document.getElementById('ferrariYillikPerformansChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: years,
                datasets: [
                    {
                        label: 'Podyum',
                        data: podyum,
                        borderColor: 'rgba(255,0,0,1)',
                        backgroundColor: 'rgba(255,0,0,0.1)',
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: { display: true, text: 'Yıllara Göre Podyum' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Podyum' } }
                }
            }
        });
    }
});

// EN BAŞARILI SEZONLAR (Galibiyet ve Puan)
Papa.parse('Analyse/ferrari_en_basarili_sezonlar.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        const years = data.map(row => row['year']);
        const galibiyet = data.map(row => Number(row['Galibiyet']));
        const puan = data.map(row => Number(row['Puan']));
        const ctx = document.getElementById('ferrariEnBasariliSezonlarChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: years,
                datasets: [
                    {
                        label: 'Galibiyet',
                        data: galibiyet,
                        backgroundColor: 'rgba(255,0,0,0.7)'
                    },
                    {
                        label: 'Puan',
                        data: puan,
                        type: 'line',
                        borderColor: 'rgba(200,0,0,1)',
                        backgroundColor: 'rgba(200,0,0,0.1)',
                        yAxisID: 'y1',
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                interaction: { mode: 'index', intersect: false },
                stacked: false,
                plugins: {
                    legend: { display: true },
                    title: { display: true, text: 'En Başarılı Sezonlar (Galibiyet & Puan)' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Galibiyet' } },
                    y1: {
                        beginAtZero: true,
                        position: 'right',
                        grid: { drawOnChartArea: false },
                        title: { display: true, text: 'Puan' }
                    }
                }
            }
        });
    }
});

// KARŞILAŞTIRMALI ANALİZ (En Çok Puan Alan 10 Takım)
Papa.parse('Analyse/ferrari_karsilastirmali_analiz.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        const takimlar = data.map(row => row['constructor_name']);
        const puan = data.map(row => Number(row['Puan']));
        const ctx = document.getElementById('ferrariKarsilastirmaliChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: takimlar,
                datasets: [
                    {
                        label: 'Puan',
                        data: puan,
                        backgroundColor: 'rgba(255,0,0,0.7)'
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: { display: true, text: 'En Çok Puan Alan 10 Takım' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Puan' } }
                }
            }
        });
    }
});

// SEZON PİLOT HEATMAP (Her pilotun sezonluk podyum sayısı - örnek heatmap)
Papa.parse('Analyse/ferrari_sezon_pilot_ozet.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        // Yıl ve pilot bazında podyumları topluca göstermek için bir heatmap datası oluşturulabilir.
        // Basit bir örnek: Her yıl en çok podyum yapan 5 pilotun podyum sayısı
        const years = [...new Set(data.map(row => row['year']))];
        const pilots = [...new Set(data.map(row => row['driver_name']))];
        // Sadece ilk 5 pilotu alalım (en çok podyum yapanlar)
        const pilotPodyum = {};
        pilots.forEach(pilot => { pilotPodyum[pilot] = Array(years.length).fill(0); });
        data.forEach(row => {
            const yearIdx = years.indexOf(row['year']);
            if (yearIdx !== -1) pilotPodyum[row['driver_name']][yearIdx] = Number(row['Podyum']);
        });
        const topPilots = pilots.slice(0, 5);
        const datasets = topPilots.map((pilot, i) => ({
            label: pilot,
            data: pilotPodyum[pilot],
            borderWidth: 2,
            fill: false,
            borderColor: `hsl(${i*60}, 80%, 50%)`,
            backgroundColor: `hsl(${i*60}, 80%, 70%)`,
            tension: 0.3
        }));
        const ctx = document.getElementById('ferrariSezonPilotHeatmapChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: years,
                datasets: datasets
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: true },
                    title: { display: true, text: 'Sezonlara Göre En Çok Podyum Yapan 5 Pilot' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Podyum' } }
                }
            }
        });
    }
});

// DASHBOARD (Yıllara göre toplam puan ve galibiyet - özet)
Papa.parse('Analyse/ferrari_yillik_ozet.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;
        const years = data.map(row => row['year']);
        const puan = data.map(row => Number(row['Puan']));
        const galibiyet = data.map(row => Number(row['Galibiyet']));
        const ctx = document.getElementById('ferrariDashboardChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: years,
                datasets: [
                    {
                        label: 'Puan',
                        data: puan,
                        backgroundColor: 'rgba(255,0,0,0.5)'
                    },
                    {
                        label: 'Galibiyet',
                        data: galibiyet,
                        backgroundColor: 'rgba(200,0,0,0.7)'
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: true },
                    title: { display: true, text: 'Ferrari Dashboard: Yıllık Puan & Galibiyet' }
                },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Değer' } }
                }
            }
        });
    }
}); 