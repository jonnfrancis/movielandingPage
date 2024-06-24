/*** show navbar ***/
const showNavbar = (toggleId, navId, bodyId, headerId) => {
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)


    // validate the variables //
    if (toggle && nav && bodypd && headerpd) {
        toggle.addEventListener('click', () => {
            //show navbar
            nav.classList.toggle('show')
            //change icon
            toggle.classList.toggle('la-times')
            //add pading to body
            bodypd.classList.toggle('body-pd')
            //add padding to header
            headerpd.classList.toggle('body-pd')
        })
    }
}

showNavbar('header-toggle', 'nav-bar', 'body-pd', 'header')

/*** link active ***/
// const linkColor = document.querySelectorAll('.nav__link')

// function colorLink() {
//     if (linkColor) {
//         linkColor.forEach(l => l.classList.remove('active'))
//         this.classList.add('active')
//     }
// }

// linkColor.forEach(l => l.addEventListener('click', colorLink))

$(document).ready(function() {
    // Initial active class based on the current URL
    var path = window.location.pathname;
    if (path.includes("categories")) {
        $("#tags-link").addClass("active");
    } else if (path.includes("actors")) {
        $("#actors-link").addClass("active");
    } else if (path.includes("directors")) {
        $("#directors-link").addClass("active");
    } else {
        $("#genres-link").addClass("active");
    }

    // Click event to toggle active class
    $(".nav__link").click(function(e) {
        $(".nav__link").removeClass("active");
        $(this).addClass("active");
    });
});


$(document).ready(function () {
    $('#autoWidth,#autoWidth2').lightSlider({
        autoWidth: true,
        loop: true,
        controls: true,
        auto: true, // Enable autoplay
        pause: 4000,
        speed: 1500, // Transition duration (in milliseconds)
        easing: 'linear',
        onSliderLoad: function () {
            $('#autoWidth,#autoWidth2').removeClass('cS-hidden');
        }
    });
});

function toggle() {
    var trailer = document.querySelector('.trailer');
    var video = document.querySelector('iframe');
    trailer.classList.toggle('active')
    video.currentTime = 0;
    video.pause()
}

$('.slider').slick({
    autoplay: false,
    speed: 800,
    lazyload: 'progressive',
    arrows: true,
    dots: false,
    prevArrow: '<div class="slick-nav prev-arrow"><i class="bx bx-chevron-r"></i></div>',
    nextArrow: '<div class="slick-nav next-arrow"><i class="bx bx-chevron-left"></i></div>',
    responsive: [{
        breakpoint: 992,
        settings: {
            dots: true,
            arrows: false,
        }
    }]
}).slickAnimation();
$(".slick-nav").on("click touch", {
    passive: true
}, function (e) {
    e.preventDefault();

    var arrow = $(this);

    if (!arrow.hasClass('animate')) {
        arrow.addClass('animate');
        setTimeout(() => {
            arrow.removeClass('animate');
        }, 1600);
    }
});
/*
var data;
function getanswer(q){
$.get("https://www.omdbapi.com/?s="+q+"&apikey=365f49b1", function(rawdata){
var rawstring =JSON.stringify(rawdata);
console.log(rawstring);
data =JSON.parse(rawstring);
var title = data.Search[0].Title;
var year = data.Search[0].Year; 
var imdburl="https://www.imdb.com/title/"+data.Search[0].imdbID+"/";

var posterurl =data.Search[0].Poster;
var rating = data.Search[0].Rated;
document.getElementById('pass').innerHTML="<h1>"+title+"</h1><br> <img src= '"+posterurl+"'><br><p> Year Released:"+year+"</p> <br> <p> Rating: "+rating+"</p> <br> <p> IMDB page: <a href='"+imdburl+"'target='_blank'>"+imdburl+"</a></p>"; }); }
*/

/*
$(document).ready(function() {

    var apikey = "365f49b1"
    $("#movieForm").submit(function(event) {
        event.preventDefault() 

        var movie = $("#movie").val()
        var result = ""
        var url = "http://www.omdbapi.com/?apikey="+apikey

        $.ajax({
            method: 'GET',
            url:url+"&s="+movie,
            success: function(data) {
                for (const movie in data){
                   console.log(movie) 
            }
                
                $("#pass").html(result);
            }
        })

        
    })
})
*/
$(document).ready(function () {

    function highlight(word, query) {
        let check = new RegExp(query, "ig")
        return word.toString().replace(check, function (matchedText) {
            return "<u style='background-color: #A5C9CA; text-decoration: none; padding: 3px; border-radius: 3px;'>" + matchedText + "</u>"
        })
    }

    $("#result-list").hide()
    $("#list").hide()

    $(".search-input").keyup(function () {
        let search = $(this).val()
        let results = ""
        if (search == "") {
            $("#result-list").hide()
            $(".search-input").removeClass("arrow").addClass("search")
        } else {
            $(".search-input").removeClass("search").addClass("arrow")
        }

        $.getJSON("https://www.omdbapi.com/?", {
            apikey: "365f49b1",
            s: search
        }, function (data) {
            if (data.Search !== undefined) {
                $.each(data.Search, function (index, value) {
                    if (index < 2) {
                        $.getJSON("https://www.omdbapi.com/?", {
                            apikey: "365f49b1",
                            i: value.imdbID
                        }, function (movieData) {
                            if (movieData) {
                                results += '<div class="result row p-1">'
                                results += '<div class="col-sm-5 result-poster"><img src=' + movieData.Poster + ' " /></div>'
                                results += '<div class="col-sm-7 text-left">'
                                results += '<div class="movie-title">' + highlight(movieData.Title, $(".search-input").val()) + ' (' + movieData.Year + ')</div>'
                                results += '<div class="rating-div "><span class="badge h4 rating">' + movieData.imdbRating + '</span>/10</div>'
                                results += '<div class="">'
                                results += '<div class="rating-lang">Language: ' + movieData.Language + '</div>'
                                results += '</div>'
                                results += '<div class="" style="padding-top: 5px;">'
                                results += '<div>' + movieData.Plot.slice(0, 50) + '... <a href="#">Details »</a></div>'
                                results += '</div>'
                                results += '</div>'
                                results += "</div>"
                                $("#results").html(results)

                                if (/Mobi|Android/i.test(navigator.userAgent)) {
                                    $("#results").children(".result").eq(1).hide();
                                } else {
                                    $(".result").first().after("<hr>")
                                }
                            }
                        })
                    }
                });
                $("#result-list").show()
            }
        });
    });

    // Function to handle search
    function handleSearch(e) {
        e.preventDefault(); // Prevent the default form submission
        var search = $(".search-input").val();
        let listResults = "";
        $("#search").hide();
        $("#pass2").hide();
        $("#list").show();
        $("#search-term").html("Results for: " + search);
        $.getJSON("https://www.omdbapi.com/?", {
            apikey: "365f49b1",
            s: search
        }, function (listData) {
            if (/Mobi|Android/i.test(navigator.userAgent)) {
                $("#list-count").html("(" + listData.totalResults + ")");
            } else {
                $("#list-count").html(listData.totalResults + " movie found");
            }
            if (listData.Search !== undefined) {
                $.each(listData.Search, function (index, value) {
                    $.getJSON("https://www.omdbapi.com/?", {
                        apikey: "365f49b1",
                        i: value.imdbID
                    }, function (listMovieData) {
                        if (listMovieData) {
                            listResults += '<div class="list-result col-6 p-3">';
                            listResults += '<div class="row" style="align-items: center;">';
                            listResults += '<div class="col-md-6 movielink-poster" style=" display: flex; align-items: center; background: url(' + listMovieData.Poster + ');"><img src="' + listMovieData.Poster + '" style="width: 50%; border-radius: 3px; position: relative; z-index: 1; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);" class="poster-img " /></div>';
                            listResults += '<div class="col-md-6 my-3 text-left">';
                            listResults += '<div class="movie-title" style="color: white;">' + highlight(listMovieData.Title, $(".search-input").val()) + ' (' + listMovieData.Year + ')</div>';
                            listResults += '<div class="rating-div" style="color: white; padding-top: 5px;"><i class="bx bxs-star" style="color: #2C74B3; font-size: 24px; margin-right: 3px;"></i><span class="h4 rating" style="color: #A5C9CA; font-weight: 700; ">' + listMovieData.imdbRating + '</span>/10</div>';
                            listResults += '<div class="my-3" style="background: rgba(26, 55, 77, 0.5); border-radius: 7px; padding-block: 7px; padding-inline: 10px;">';
                            listResults += '<div style="color: white;"><strong>Language:</strong> ' + listMovieData.Language + '</div>';
                            listResults += '<div style="color: white;"><strong>Stars:</strong> ' + listMovieData.Actors.split(",").slice(0, 3) + '</div>';
                            listResults += '<div style="color: white;"><strong>Genre:</strong> ' + listMovieData.Genre.split(",").slice(0, 3) + '</div>';
                            listResults += '</div>';
                            listResults += '<div class="my-3">';
                            listResults += '<div style="color: rgb(231, 246, 242); display: -webkit-box; -webkit-line-clamp: 6; overflow: hidden; text-overflow: ellipsis;">' + listMovieData.Plot + '</div>';
                            listResults += '</div>';
                            listResults += '</div>'; // col-6 end
                            listResults += "</div>"; // row end
                            listResults += "</div>"; // list-result col-6 end
                            $("#list-results").html(listResults);
                            $(".list-result:odd:not(:last-child)").after("<div class='col-12'><hr></div>");
                        }
                    });
                });
            }
        });
    }

    // Bind click event
    $("#show-more").click(function (e) {
        handleSearch(e);
    });

    // Bind keydown event for Enter key
    $(".search-input").keydown(function (e) {
        if (e.key === "Enter") { // Check if the key pressed is Enter
            handleSearch(e);
        }
    });


    $("#searchAgain").click(function () {
        $("#search").show()
        $("#list").hide()
        $("#result-list").hide()
        $(".search-input").val("")
        $("#pass2").show()
    });
});

$(function () {
    $(".search-input")
        .popover({
            title: 'WAIT!!!',
            content: "You can't do that. Go search from home😅"
        })
        .blur(function () {
            $(this).popover('hide');
        });
});


document.addEventListener('DOMContentLoaded', function () {
    const loadMoreBtn = document.getElementById('load-more-btn');
    let displayedMovies = 6;

    loadMoreBtn.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent default button behavior

        const hiddenMovies = document.querySelectorAll('#movies-list .movies-box.hidden');
        for (let i = 0; i < 6 && i < hiddenMovies.length; i++) {
            hiddenMovies[i].classList.remove('hidden');
        }
        displayedMovies += 6;

        // Hide the Load More button if all movies are displayed
        if (hiddenMovies.length <= 6) {
            loadMoreBtn.style.display = 'none';
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const loadMoreBtn = document.getElementById('load-more-actors');
    let displayedActors = 14;

    loadMoreBtn.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent default button behavior

        const hiddenMovies = document.querySelectorAll('#tagsh .category-list .actors-box.hidden');
        for (let i = 0; i < 12 && i < hiddenMovies.length; i++) {
            hiddenMovies[i].classList.remove('hidden');
        }
        displayedActors += 6;

        // Hide the Load More button if all movies are displayed
        if (hiddenMovies.length <= 6) {
            loadMoreBtn.style.display = 'none';
        }
    });
});