document.addEventListener('DOMContentLoaded', function() {
    // Manejo de la barra de progreso
    window.addEventListener('scroll', function() {
        let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        let scrolled = (winScroll / height) * 100;
        document.getElementById("myProgressBar").style.width = scrolled + "%";
    });

    // Manejo del formulario de comentarios
    const commentForm = document.querySelector('form');
    if (commentForm) {
        commentForm.addEventListener('submit', function() {
            localStorage.setItem('scrollPosition', window.pageYOffset);
        });
    }

    // Restaurar la posición del scroll
    window.addEventListener('load', function() {
        const savedPosition = localStorage.getItem('scrollPosition');
        if (savedPosition) {
            setTimeout(function() {
                window.scrollTo(0, parseInt(savedPosition));
                localStorage.removeItem('scrollPosition');
            }, 100);
        }
    });
});