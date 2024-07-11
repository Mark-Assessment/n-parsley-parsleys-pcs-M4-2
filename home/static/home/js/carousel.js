$(document).ready(function () {
    $("#discounted-products-carousel, #featured-products-carousel").owlCarousel({
        items: 4,
        loop: true,
        margin: 10,
        pagination: false,
        navigation: true,
        autoPlay: 3000,
        stopOnHover: true,
        navigationText: ["<", ">"],
        responsive: {
            0: {
                items: 1,
            },
            600: {
                items: 2,
            },
            800: {
                items: 3,
            },
            1000: {
                items: 3,
            },
            1500: {
                items: 4,
            }
        }
    });
});