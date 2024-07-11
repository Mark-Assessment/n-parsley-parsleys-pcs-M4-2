$(document).ready(function() {
    $("#discounted-products-carousel, #featured-products-carousel").owlCarousel({
        items: 4,
        loop: true,
        margin: 10,
        nav: true,
        responsive: {
            0: {
                items: 1,
                nav: true
            },
            600: {
                items: 2,
                nav: true
            },
            1000: {
                items: 4,
                nav: true
            }
        }
    });
});